"""
  Implement your own _map function.
  first arg is collection, second arg - callback (mapper) 
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.
"""
new_list = [4, 15, 25, 1, 2, 17, 0.5, 6]

''' SZ
  Please install pylint or read this convention https://www.python.org/dev/peps/pep-0008/

  [pylint] C0326:No space allowed before bracket
'''

def my_map(x):
    x = x % 2
    return x

def _map(coll, func):
    lst = []
    for n in coll:
        lst.append(func(n))
    return lst

print(_map(new_list, my_map))
#done 03/26