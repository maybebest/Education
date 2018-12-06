"""
  Implement your own _uniq function.
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden.
"""

'''SZ (not for rework) It could be written more efficient with dictionary.

def __uniq(collection):
    _hash = {}
    new_collection = []

    for x in collection:
        if _hash.get(x, None):
            continue
        new_collection.append(x)
        _hash[x] = True

    return new_collection

print(_uniq(list(range(20000)))) # exited with code=0 in 2.533 seconds
print(__uniq(list(range(20000)))) # exited with code=0 in 0.064 seconds

#for i in collection:
#   if i not in new_collection:

I believe "in" is a cycle operation too (under cut) 
so you have an O(n^2) algorithm approximately (cycle in cycle)
'''

my_collection = (1,2,55,4,5,4,7)

def _uniq(collection):
    new_collection = []
    for x in collection:
        new_collection.append(x) if x is not new_collection else None
    return new_collection

print(_uniq(my_collection))