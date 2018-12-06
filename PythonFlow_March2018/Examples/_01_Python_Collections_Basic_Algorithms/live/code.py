
'''AM
Please use double quotes here
'''
print('Hello')


my_dict = {1: 'test'}

print(my_dict.keys())
a = {1,2,3}
b = {1,2,3}
print(id(a), id(b))

print({1,2,3} is {1,2,3})


NUMBERS = [2,3,4,5,6]

RESULT = map(lambda n: n * 2, NUMBERS)

print(tuple(RESULT))
print(list(RESULT))