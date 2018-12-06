"""_unique()
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden. 
"""
# lst = ['Jack', 27, 'USA', 5, "Jack", 'New York', 27, 44, 44]

def _unique(collect):
    output = []
    for i in collect:
        if i not in output:
            output.append(i)
    return output

'''AM (not for rework)
It could be written more efficient with dictionary.
def my_uniq(coll):
    _hash = {}
    result = []
    for el in coll:
        if _hash.get(el, None): # dictionary here more efficient then " if collect[i] not in output:"
            continue
        result.append(el)
        _hash[el] = 1
    return result

print(my_uniq(tuple(range(20000)))) ~ 0.5 seconds
print(_unique(tuple(range(20000)))) ~ 5 seconds

# for i in range(0, length):
#     if collect[i] not in output: 
#### i believe "in" is a cycle operation too (under cut) 
#### so you have an O(n^2) algorithm approximately (cycle in cycle)
 
'''

# print(_unique(tuple(range(10000))))
#print (_unique(lst))