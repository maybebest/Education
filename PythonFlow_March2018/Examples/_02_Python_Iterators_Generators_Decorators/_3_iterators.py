"""Iterators."""

LANG = 'Python'

LANG_ITERATOR = iter(LANG)

print(LANG_ITERATOR.__next__())  # P

print(next(LANG_ITERATOR))  # y

print(next(LANG_ITERATOR))  # t

for char in LANG_ITERATOR:
    print(char, end=' ')  # h o n

print(next(LANG_ITERATOR))
"""
File "<file>", <line>, in <module>
    print(next(LANG_ITERATOR))  
StopIteration
"""
