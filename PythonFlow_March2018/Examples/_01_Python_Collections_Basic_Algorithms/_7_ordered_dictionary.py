"""OrderedDict"""

from collections import OrderedDict

LETTERS = [('c', 2), ('b', 1), ('d', 3), ('a', 0)]

VALUES = OrderedDict(LETTERS)
print(list(VALUES.keys()))
# ['c', 'b', 'd', 'a']

VALUES = dict(LETTERS)
print(list(VALUES.keys()))
# ['d', 'a', 'b', 'c']
