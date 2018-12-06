'''
- Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.
'''

''' SZ
  Please install pylint or read this convention https://www.python.org/dev/peps/pep-0008/

  [pylint] C0326:No space allowed before bracket
'''

def own_find(my_function, my_collection):
    for n in my_collection:
      if my_function(n):
        return n
    return False

def find_neche(x):
  return x % 2 != 0

collection = [2,4,6,11]
print(own_find(find_neche, collection))
