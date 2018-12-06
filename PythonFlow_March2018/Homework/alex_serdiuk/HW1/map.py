"""Implement your own _map function.
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden."""

def minus(n):
    return n - 2*2

def my_map(callback, collection):
    new_col = []
    for item in collection:
        if callback(item):
            new_col.append(callback(item))
    return new_col

test_data = [1, 2, 3, 3, 4, 5, 5, 7, 2, 3]

print(my_map(minus, test_data))

