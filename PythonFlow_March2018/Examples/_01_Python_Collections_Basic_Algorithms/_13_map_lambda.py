"""Map. lambda"""

import math

CIRCLES_R = [3, 4, 5]

CIRCLES_S = map(lambda r: math.pi * (r ** 2), CIRCLES_R)

# [28.274333882308138, 50.26548245743669, 78.53981633974483]
print(list(CIRCLES_S))
print(tuple(CIRCLES_S))  # ()

CIRCLES_L = map(lambda r: 2 * math.pi * r, CIRCLES_R)

# (18.84955592153876, 25.132741228718345, 31.41592653589793)
print(tuple(CIRCLES_L))

REC_SIDES = [(2, 5), (6, 8)]

REC_SQUARES = map(lambda xy: (xy[0] * xy[1],), REC_SIDES)

print(list(REC_SQUARES))  # [(10,), (48,)]
