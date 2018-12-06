'''
- Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden.
'''

''' SZ
  Please install pylint or read this convention https://www.python.org/dev/peps/pep-0008/

  [pylint] C0326:No space allowed before bracket
'''


def own_filter(my_function, my_collection):
    result = []
    for n in my_collection:
      if my_function(n):
        result.append(n)
    return result

def filter_che(x):
  return x % 2 == 0

collection = [1,3,6,8]
print(own_filter(filter_che, collection))
