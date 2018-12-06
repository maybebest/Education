
"""Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden."""

def range(x):
    return 2 < x <= 6

def special_filter(callback, collection):
    expected = []
    for item in collection:
        if callback(item):
            expected.append(item)
    return expected

test_data = [1, 2, 3, 3, 4, 5, 5, 7, 2, 3]

print(special_filter(range, test_data))