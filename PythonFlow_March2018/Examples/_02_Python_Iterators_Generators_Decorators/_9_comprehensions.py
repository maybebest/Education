

"""Comprehension"""

MY_LIST = []
for x in range(5):
    MY_LIST.append(x * 2)

print(MY_LIST)  # [0, 2, 4, 6, 8]

MY_LIST = list(range(0, 10, 2))

print(MY_LIST)  # [0, 2, 4, 6, 8]

MY_LIST = [x * 2 for x in range(5)]

print(MY_LIST)  # [0, 2, 4, 6, 8]
