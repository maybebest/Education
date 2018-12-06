'''
- Implement your own _map function.
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.
'''

''' SZ
  Please install pylint or read this convention https://www.python.org/dev/peps/pep-0008/

  [pylint] C0326:No space allowed before bracket
'''

def own_map(my_function, my_collection):
    result = []
    for n in my_collection:
        result.append(my_function(n))
    return result

def func(x):
  x = x * 2
  return x

collection = [1,3,6,8]
print(own_map(func, collection))
