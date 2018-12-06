"""OrderedDict"""

from collections import OrderedDict

LETTERS = [('c', 2), ('b', 1), ('d', 3), ('a', 0)]

VALUES = OrderedDict(LETTERS)
VALUES['e'] = 4

print(list(VALUES.keys()))
# ['c', 'b', 'd', 'a', 'e']

del VALUES['a']

VALUES['a'] = 5
print(list(VALUES.keys()))
# ['c', 'b', 'd', 'e', 'a']

print(list(VALUES.values()))
# [2, 1, 3, 4, 5]
