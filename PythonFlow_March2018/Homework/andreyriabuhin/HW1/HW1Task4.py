"""
  Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.
"""
''' SZ
  Please install pylint or read this convention https://www.python.org/dev/peps/pep-0008/

  [pylint] C0326:No space allowed before bracket
'''

def my_find(my_fun, my_coll):
    for i in my_coll:
      if my_fun(i):
        return i
    return False

def find_fun (x):
  return x % 2 <= 0

collect = [7,20,15,4]
print(my_find(find_fun, collect))
#done 03/26