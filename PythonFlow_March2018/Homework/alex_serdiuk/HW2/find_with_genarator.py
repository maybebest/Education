
""""- Implement your own _find function using generator expression.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  generator expression usage required."""

test_data = [1, 2, 3, 3, 4, 5, 5, 9, 7, 2, 3]

def dop(n):
    return n >= 8

def my_find(callback, collection):
    return next((item for item in collection if callback(item)), "Something interesting!")

print(my_find(dop, test_data))

"""SZ
        this function returns a generator, but should returns first found value
        for exmaple like this
        return next((<your gen expression here>), 'no matches')
"""

"""
def dop(n):
    return n >= 4
    
    for item in collection:
        if callback(item) == True:
            yield item

test_data = [1, 2, 3, 3, 4, 5, 5, 9, 7, 2, 3]
this_iter = my_find(dop, test_data)

print(next(this_iter))
print(next(this_iter))
print(next(this_iter))
print(next(this_iter))

"""