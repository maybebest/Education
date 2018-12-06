"""
- Create iterator from tuple which created using comprehension
  print values using: next, loop
"""
from Homework.jamalzeynalov import items_collection

my_tuple = tuple(x for x in items_collection)

my_iter = iter(my_tuple)

while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
