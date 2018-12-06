"""
  Implement your own _uniq function.
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden.
"""

'''SZ (not for rework) It could be written more efficient with dictionary.

def _new_function(collection):
    _hash = {}
    result = []

    for i in collection:
        if _hash.get(i, None):   # GK: Looks nice, I will try this
            continue
        result.append(i)
        _hash[i] = True    # GK: Why do we need this statement?

    return result
print(new_function(list(range(20000)))) # exited with code=0 in 2.533 seconds
print(_new_function(list(range(20000)))) # exited with code=0 in 0.064 seconds

#for i in collection:
#   if i not in new_collection:

I believe "in" is a cycle operation too (under cut) 
so you have an O(n^2) algorithm approximately (cycle in cycle)
'''

def new_function(collection):
    new_collection = []
    for i in collection:
        if i not in new_collection:
            new_collection.append(i)

    print("Given collection: " + str(collection))
    print("New collection: " + str(new_collection))
    return new_collection

my_list = [1, 4, 6, 4, 7, 8, 8, 4]

''' SZ
    I expect that function returns mapped collection but without return statement it returns None.
    Please add return statement to new_function

    mapped_list = new_function(my_list)
    print(mapped_list) # None
'''

new_list = new_function(my_list)
print(new_list)


