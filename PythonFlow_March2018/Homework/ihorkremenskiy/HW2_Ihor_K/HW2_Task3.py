'''
- Create iterator from tuple which created using comprehension
  print values using: next, loop
'''
my_list = [4, 8, 15, 16, 23, 42]

tuple_iter = iter(tuple(x ** 2 for x in my_list))

print("My class is: ", type(tuple_iter), '\n')

print("2 first results:")

print(next(tuple_iter))
print(next(tuple_iter))

print("Other results:")

for item in tuple_iter:
    print(item)
