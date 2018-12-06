"""Generator Expression"""

from sys import getsizeof

LIST_COMP = [x ** 2 for x in range(100) if x % 2 == 0]

GEN_EXP = (x ** 2 for x in range(100) if x % 2 == 0)

print(LIST_COMP, getsizeof(LIST_COMP))
# [0, 4, 16, 36, 64 ... 9604] 528

print(GEN_EXP, getsizeof(GEN_EXP))
# <generator object <genexpr> at 0x7f03649b50f8> 88

print(next(GEN_EXP))  # 0
