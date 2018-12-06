def sqr(number):
    return number ** 2
my_list = [1, 2, 3, 4, 3, 2, 1]

'''SZ (not for rework) It could be written more efficient with dictionary.

def _remove_duplicates(my_list):
    _hash = {}
    result = []

    for x in my_list:
        if _hash.get(x, None):
            continue
        result.append(x)
        _hash[x] = True

    return result

print(remove_duplicates(list(range(20000)))) # exited with code=0 in 2.533 seconds
print(_remove_duplicates(list(range(20000)))) # exited with code=0 in 0.064 seconds

#for x in my_list:
#    if x not in res:

I believe "in" is a cycle operation too (under cut) 
so you have an O(n^2) algorithm approximately (cycle in cycle)

'''

def remove_duplicates(my_list):
    """
    Implement your own _uniq function.
    first arg is collection.
    function returns new collection of uniq items
    Usage of Set data structures is forbidden.
    """
    res = []
    for x in my_list:
        if x not in res:
            res.append(x)
    return res

print(remove_duplicates(my_list))

'''
def my_map(list, call_back_function):
    """
    Implement your own _map function.
    first arg is collection, second arg - callback (mapper)
    function returns new collection of mapped items.
    Usage of standard map functionality is forbidden.
    """
    new_list = []
    for n in list:
         SZ
            Wrong implementation.
            Please execute the given callback for each element of the given collection
            and create list with results of callback executions and return it.

        new_list.append(sqr(n))
    return call_back_function(new_list)

print(my_map(my_list, remove_duplicates))
'''
def my_map(list, call_back_function):
    new_list = []
    for n in list:
        new_list.append(call_back_function(n))
    return new_list

print(my_map(my_list, sqr))


def check_callback(value):
    if value > 2:
        return True
    return False


def my_find(callback, list_):
    """
    Implement your own _find function.
    first arg is callback, second arg - collection.
    function returns first item from collection for which callback function call return true
    Usage of standard filter function or yor own _filter is forbidden.
    """
    for some in list_:
        if callback(some):
            return some
    return False

print(my_find(check_callback,my_list))


def module_by(x):
    if x % 2 == 0:
        return True
    return False


def my_filt(callback, list_):
    """
    Implement your own _filter function.
    first arg is callback, second arg - collection.
    function returns new collection of items for which callback function call return true
    Usage of standard filter function is forbidden.
    """
    res = []
    for some in list_:
        if callback(some):
            res.append(some)
    return res

print(my_filt(module_by,my_list))

a = [1,2]
a = [1,2]