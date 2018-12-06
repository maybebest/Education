"""Implement your own _uniq function.
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden."""

'''AM (not for rework)
It could be written more efficient with dictionary.
def my_uniq(coll):
    _hash = {}
    result = []
    for el in coll:
        if _hash.get(el, None): # dictionary here more efficient then "if item in expected:"
            continue
        result.append(el)
        _hash[el] = 1
    return result

print(my_uniq(tuple(range(20000)))) ~ 0.5 seconds
print(very_uniq(tuple(range(20000)))) ~ 5 seconds

# for item in collection:
#     if item in expected:
#### i believe "in" is a cycle operation too (under cut) 
#### so you have an O(n^2) algorithm approximately (cycle in cycle)
 
'''

def very_uniq(collection):
    expected = []
    for item in collection:
        if item in expected:
            pass
        else:
            expected.append(item)
    return expected


test_data = [1, 2, 3, 3, 4, 5, 5, 7, 2, 3]

print(very_uniq(test_data))
