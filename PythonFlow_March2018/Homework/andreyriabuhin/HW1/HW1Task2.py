"""
  Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden.
"""

''' SZ
  Please install pylint or read this convention https://www.python.org/dev/peps/pep-0008/

  [pylint] C0326:No space allowed before bracket
'''
def my_filt(my_function, my_collection):
    result = []
    for n in my_collection:
      if my_function(n):
        result.append(n)
    return result

def filt_one(x):
  return x % 2 == 0

collection = [0,4,7,16,5]
print(my_filt(filt_one, collection))
# done 03/26