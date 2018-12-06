"""Comprehension"""

MY_DICT = {x: chr(65 + x) for x in range(0, 5)}

print(type(MY_DICT))  # <class 'dict'>
print(MY_DICT)  # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

MY_SET = {x ** 3 for x in range(10) if x % 2 == 0}

print(type(MY_SET))  # <class 'set'>
print(MY_SET)  # {0, 8, 64, 512, 216}
