# _filter function.
#  first arg is callback, second arg - collection.
#  function returns new collection of items for which callback function call return true
#  Usage of standard filter function is forbidden


tup = tuple(range(15))

def is_odd_number(x):
     return (x % 2) == 0

def _filter(func, coll):
    out = []
    for i in coll:
        if func(i):
           out.append(i)
    return out

print(_filter(is_odd_number, tup))
