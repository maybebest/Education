"""
- Implement your own _find function using generator expression.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  generator expression usage required.
"""
from Homework.jamalzeynalov import items_collection
from Homework.jamalzeynalov.HW2.decorator import my_print


@my_print
def _find(callback_fn, collection):
    return next((item for item in collection if callback_fn(item)), "No matches!")


first_match = _find(lambda x: type(x) is int, items_collection)
