## Homework 2 ##

"""- Implement generator function which returns filtered items of the given list (lazy _filter, items by request)
  print values using: next, loop"""

def range(x):
    return 2 < x <= 6

def special_filter(callback, collection):
    '''SZ (not for rework)
        This could be implemented in more elegant way
        return (item for item in collection if callback(item))
    '''
    for item in collection:
        if callback(item):
            yield item

test_data = [1, 2, 3, 3, 4, 5, 5, 7, 2, 3]
this_iter = special_filter(range, test_data)

print(next(this_iter))
print(next(this_iter))
print(next(this_iter))
print(next(this_iter))
print(next(this_iter))
print(next(this_iter))












