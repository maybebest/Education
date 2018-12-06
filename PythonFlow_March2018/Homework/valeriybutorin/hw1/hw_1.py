# Homework 1
from Homework.valeriybutorin.test_data.test_data import tuple_to_test, list_to_test
from Homework.valeriybutorin.utils.utils import to_type, is_int, map_to_string


def find_str_one(item):
    """:return item with value str value one"""

    return str(item) if "one" == str(item) else None


def get_unique_collection(collection):
    """
    - Implement your own _uniq function.
      first arg is collection.
      function returns new collection of uniq items
      Usage of Set data structures is forbidden.
    """
    unique_collection = []
    for item in collection:
        if item not in unique_collection:
            unique_collection.append(item)
    return to_type(collection, unique_collection)


'''AM (not for rework)
It could be written more efficient with dictionary.
def my_uniq(coll):
    _hash = {}
    result = []
    for el in coll:
        if _hash.get(el, None): # dictionary here more efficient then "if item not in unique_collection:"
            continue
        result.append(el)
        _hash[el] = 1
    return result

print(my_uniq(list(range(20000)))) ~ 0.5 seconds
print(get_unique_collection(list(range(20000)))) ~ 5 seconds

# for item in collection:
#     if item not in unique_collection:
#### i believe "in" is a cycle operation too (under cut) 
#### so you have an O(n^2) algorithm approximately (cycle in cycle) 
'''

print("\r\nImplement your own _uniq function: return collection where all items are unique")
print(get_unique_collection(list_to_test))
print(get_unique_collection(tuple_to_test))


def filter_by_type(func, collection):
    """
    - Implement your own _filter function.
      first arg is callback, second arg - collection.
      function returns new collection of items for which callback function call return true
      Usage of standard filter function is forbidden.
    """
    filter_collection = []
    for item in collection:
        if func(item):
            filter_collection.append(item)
    return to_type(collection, filter_collection)


print("\r\nImplement your own _filter function: filter all items by int type")
print(filter_by_type(is_int, list_to_test))
print(filter_by_type(is_int, tuple_to_test))


def map_items_to_str(collection, map_func):
    """
    - Implement your own _map function.
      first arg is collection, second arg - callback (mapper)
      function returns new collection of mapped items.
      Usage of standard map functionality is forbidden.
    """
    collection_with_str = []
    for item in collection:
        collection_with_str.append(map_func(item))
    return to_type(collection, collection_with_str)


print("\r\nImplement your own _map function: map all items to str")
print(map_items_to_str(list_to_test, map_to_string))
print(map_items_to_str(tuple_to_test, map_to_string))

"""
- Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.
"""


def find_first_element_by_type(func, collection):
    for item in collection:
        if func(item):
            return item


print("\r\nImplement your own _find function: find str with value one")
print(find_first_element_by_type(find_str_one, list_to_test))
print(find_first_element_by_type(find_str_one, list_to_test))
