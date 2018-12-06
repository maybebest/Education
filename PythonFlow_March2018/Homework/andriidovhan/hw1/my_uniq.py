'''AM (not for rework)
It could be written more efficient with dictionary.
def __uniq(coll):
    _hash = {}
    result = []
    for el in coll:
        if _hash.get(el, None): # dictionary here more efficient then "if i in result:"
            continue
        result.append(el)
        _hash[el] = 1
    return result

print(__uniq(list(range(20000)))) ~ 0.5 seconds
print(my_uniq(list(range(20000)))) ~ 5 seconds

# for i in some_list:
#     if i in result:
#### i believe "in" is a cycle operation too (under cut) 
#### so you have an O(n^2) algorithm approximately (cycle in cycle) 
'''

def my_uniq(some_list):
    result = []
    for i in some_list:
        if i in result:
            pass
        else:
            result.append(i)
    return result

NUMBERS = [1, 1, 2, 2, 2, 3, 4, 5]

print(my_uniq(NUMBERS))