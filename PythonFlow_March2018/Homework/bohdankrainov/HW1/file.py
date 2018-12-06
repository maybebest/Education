collection = [1, 2, 3, 4, 5, 3, 24, 1, 2, 4, 7, 3, 56, 5, 7, 8, 24]
print('Collection:', collection)

# my uniq function
'''AM (not for rework)
It could be written more efficient with dictionary.
def __uniq(coll):
    _hash = {}
    result = []
    for el in coll:
        if _hash.get(el, None): # dictionary here more efficient then "if i not in res:"
            continue
        result.append(el)
        _hash[el] = 1
    return result

print(__uniq(tuple(range(20000)))) ~ 0.5 seconds
print(my_uniq(tuple(range(20000)))) ~ 5 seconds

# for i in col:
#     if i not in res:
#### i believe "in" is a cycle operation too (under cut) 
#### so you have an O(n^2) algorithm approximately (cycle in cycle)
 
'''


def my_uniq(col):
    res = []
    for i in col:
        if i not in res:
            res.append(i)
    return res


print('uniq: ' + str(my_uniq(collection)))

# my filter function


def my_filter(callback_func, col):
    res = []
    for i in col:
        if callback_func(i):
            res.append(i)
    return res


def check_odd(a):
    return True if a % 2 == 0 else False


print('filter: ' + str(my_filter(check_odd, collection)))

# my map function


def my_map(callback_func, col):
    return [callback_func(i) for i in col]


def double(i):
    return i*2


print('map: ' + str(my_map(double, collection)))

# my find function


def my_find(callback_func, col):
    for i in col:
        if callback_func(i):
            return i


def filter_check(i):
    if i % 8 == 0:
        return i


print('find: ' + str(my_find(filter_check, collection)))
