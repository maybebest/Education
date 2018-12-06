'''AM
ModuleNotFoundError: No module named 'Homework'
Please use relative imports inside your package.
'''
from Homework.valeriybutorin.test_data.test_data import iterator_to_test
from Homework.valeriybutorin.utils.utils import is_odd
"""
- Implement your own _find function using generator expression.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  generator expression usage required.
"""

'''AM
Please use generator expression here:

def generator_find(func, collection): #collection could be just a list or tuple, not exact iterator
    return next((<<your generator expression here>>), None)
'''


def generator_find(func, collection):
    return next((item for item in collection if func(is_odd(item))), None)


print("First odd number from the collection:", generator_find(is_odd, iterator_to_test))
