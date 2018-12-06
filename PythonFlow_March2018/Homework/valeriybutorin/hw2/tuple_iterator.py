from Homework.valeriybutorin.test_data.test_data import tuple_with_ints_to_test

"""
- Create iterator from tuple which created using comprehension
  print values using: next, loop
"""

tuple_iterator = iter(tuple_with_ints_to_test)

print("Print value by next: ", next(tuple_iterator))
print("Print value in loop: ", tuple(number for number in tuple_iterator))
