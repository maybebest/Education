'''
- Implement your own _uniq function.
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden.
'''

'''SZ (not for rework) It could be written more efficient with dictionary.

def __uniq(collection):
    _hash = {}
    result = []

    for i in collection:
        if _hash.get(i, None):
            continue
        result.append(i)
        _hash[i] = True

    return result

print(__uniq(list(range(20000)))) # exited with code=0 in 2.533 seconds
print(_uniq(list(range(20000)))) # exited with code=0 in 0.064 seconds

I believe "in" is a cycle operation too (under cut) 
so you have an O(n^2) algorithm approximately (cycle in cycle)
'''

collection = (1,3,6,8,8,8,1,125,12, 'star', 'star', 'bucks', 'bucks')

def _uniq(generate_uniq_collection): #start uniq function with arg
        new_collection =[] #create temporary variable for the _uniq function
        for n in generate_uniq_collection: # cycle for all items in collection
            new_collection.append(n) if n not in new_collection else None # add item if it doesn't exist yet, else no actions
        return new_collection #return generated value

print(_uniq(collection)) # print my collection but after applying described above _uniq function that makes all items unique
