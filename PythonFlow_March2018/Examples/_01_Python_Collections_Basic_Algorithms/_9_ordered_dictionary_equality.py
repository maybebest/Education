"""OrderedDict"""

from collections import OrderedDict

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)  # True

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)  # False