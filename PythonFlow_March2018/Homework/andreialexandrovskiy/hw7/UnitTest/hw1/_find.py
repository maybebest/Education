"""_find()
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.
"""

lst = ['Jack', 27, 'USA', 5, "Jack", 'New York', 27, 44, 44]

def equals_five(x):
    return x == 5


def _find(func, collect):
    for i in collect:
        if func(i):
            return i
        

#print (_find(equals_five, lst))
