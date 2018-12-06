"""
- Implement generator function which returns filtered items of the given list (lazy _filter, items by request)
  print values using: next, loop
"""
from Homework.jamalzeynalov import items_collection


def _filter_generator(callback_fn, collection):
    for matched_item in [x for x in collection if callback_fn(x)]:
        yield matched_item


_filter = _filter_generator(lambda x: type(x) is int, items_collection)

'''AM (not for rework)
Could be rewritten without exception handling
while True:
    res = next(_filter, None) # None or some other def value as second param
    if res == None:
        break
    print(res)
'''
while True:
    try:
        print(next(_filter))
    except StopIteration:
        break
