
"""Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden."""

def dop(n):
    return n >= 6

def my_find(callback, collection):
    for item in collection:
        if callback(item) == True:
            return item

test_data = [1, 2, 3, 3, 4, 5, 5, 9, 7, 2, 3]

print(my_find(dop, test_data))
