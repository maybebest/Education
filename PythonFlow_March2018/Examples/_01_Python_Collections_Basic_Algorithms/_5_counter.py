"""Counter"""

from collections import Counter

C1 = Counter('abracadabra')
print(C1)
# Counter({'a': 5, 'b': 2, 'r': 2, 'd': 1, 'c': 1})

C2 = Counter('hubbabubba')
print(C2)
# Counter({'b': 5, 'a': 2, 'u': 2, 'h': 1})

C2.subtract(C1)
print(C2)
# Counter({'b': 3, 'u': 2, 'h': 1, 'c': -1, 'd': -1, 'r': -2, 'a': -3})

print(sorted(C2.elements()))
# ['b', 'b', 'b', 'h', 'u', 'u']

C2 = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(C2)
# Counter({'blue': 3, 'red': 2, 'green': 1})
