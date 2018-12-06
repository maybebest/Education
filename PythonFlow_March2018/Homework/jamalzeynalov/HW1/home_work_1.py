# items_collection = [False, None, '2', 2, 2.0, 3, 4, 5, 123456, 0, 123456, "Some string"]
from Homework.jamalzeynalov import items_collection


def my_own_uniq(collection):
    """ Implement your own _uniq function.
    first arg is collection.
    function returns new collection of uniq items
    Usage of Set data structures is forbidden.
    """
    new_collection = []
    for item in collection:
        new_collection.append(item) if item not in new_collection else None
    return new_collection


'''AM (not for rework)
Nice shot :)
One more implementation:
def my_uniq(coll):
    _hash = {}
    result = []
    for el in coll:
        if _hash.get(el, None): # dictionary here more efficient then " if item not in collection:"
            continue
        result.append(el)
        _hash[el] = 1
    return result
'''


def my_own_uniq_2(collection):
    """ Alternative way. """
    return list({x: None for x in collection}.keys())


def my_own_filter(callback_func, collection):
    """ Implement your own _filter function.
    first arg is callback, second arg - collection.
    function returns new collection of items for which callback function call return true
    Usage of standard filter function is forbidden.
    """
    return [x for x in collection if callback_func(x)]


def my_own_map(collection, mapper_func):
    """ Implement your own _map function.
    first arg is collection, second arg - callback (mapper)
    function returns new collection of mapped items.
    Usage of standard map functionality is forbidden.
    """
    return [mapper_func(x) for x in collection]


def my_own_find(callback_func, collection, to_return="No matches!"):
    """ Implement your own _find function.
    first arg is callback, second arg - collection.
    function returns first item from collection for which callback function call return true
    Usage of standard filter function or your own _filter is forbidden.
    """
    for x in collection:
        if callback_func(x):
            return x
    else:
        return to_return


'''AM (not for rework)
This is not a requirement but we work with Python 3 :)
'''
# print("my_own_uniq 1: ", sorted(my_own_uniq(items_collection)))
# print("my_own_uniq 2: ", sorted(my_own_uniq_2(items_collection)))

# print("\nmy_own_filter: ", my_own_filter(bool, items_collection))
#
# print("\nmy_own_map: ", my_own_map(items_collection, lambda x: type(x)))
# print("my_own_map (not lambda): ", my_own_map(items_collection, type))
#
# print("\nmy_own_find (success): %s" % my_own_find(lambda x: x == 123456, items_collection))
# print("my_own_find (if no matches): %s" % my_own_find(lambda x: x == "nothing", items_collection))
