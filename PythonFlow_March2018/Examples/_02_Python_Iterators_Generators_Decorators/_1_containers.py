"""Containers"""

print(1 in [1, 2, 3])  # True
print(1 in {1, 2, 3})  # True
print(1 in (1, 2, 3))  # True
print(1 in {1: 'foo', 2: 'bar', 3: 'baz'})  # True
print('1' in '123')  # True
print('12' in '123')  # True: a string "contains" all its substrings
