
""""- Create iterator from tuple which created using comprehension
  print values using: next, loop"""

MY_TUPLE = iter(tuple(i * 2 for i in (1, 2, 3, 4, 5)))

print(type(MY_TUPLE))
print(next(MY_TUPLE))
print(next(MY_TUPLE))
print(next(MY_TUPLE))

