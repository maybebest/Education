"""Iterators"""

X = [1, 2, 3]
Y = iter(X)
Z = iter(X)

print('First Y iteration: %d; Second Y iteration: %d; First Z iteration: %d;' %
      (next(Y), next(Y), next(Z)))
# First Y iteration: 1; Second Y iteration: 2; First Z iteration: 1;

print(type(X))
# <class 'list'>

print(type(Y))
# <class 'list_iterator'>

print(Y)
# <list_iterator object at 0x7f4d4ba1a908>
