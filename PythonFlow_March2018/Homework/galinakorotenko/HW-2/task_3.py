"""
Create iterator from tuple which created using comprehension
print values using: next, loop
"""

my_tuple = tuple(i.capitalize() for i in 'HelloWorld!PythonIsGreat!' if i.islower())


chars = iter(my_tuple)
for elem in chars:
    print(next(chars))
