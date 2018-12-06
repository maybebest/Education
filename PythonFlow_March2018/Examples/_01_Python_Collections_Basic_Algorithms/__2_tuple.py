"""Tuples"""

EMPTY_TUPLE = ()
print(EMPTY_TUPLE) # ()

INTEGERS_TUPLE = (1, 2, 3)
print(INTEGERS_TUPLE) # (1, 2, 3)

MIXED_TUPLE = (1, '2', 3.14)
print(MIXED_TUPLE) # (1, '2', 3.14)

NESTED_TUPLE = ('Python', [1, '2', 3.14], (1, '2', 3.14))
print(NESTED_TUPLE) # ('Python', [1, '2', 3.14], (1, '2', 3.14))

TUPLE_WITHOUT_PARENTHESES = 1, '2', 3.14
print(TUPLE_WITHOUT_PARENTHESES) # (1, '2', 3.14)

a, b, c = TUPLE_WITHOUT_PARENTHESES
print(a, b, c) # 1 2 3.14
'''Creating a tuple with one element is a bit tricky.
Having one element within parentheses is not enough. 
We will need a trailing comma to indicate that it is in fact a tuple.
'''
# only parentheses is not enough
MY_TUPLE = ("Python")
print(type(MY_TUPLE))  # <class 'str'>

# need a comma at the end
MY_TUPLE = ("Python",)
print(type(MY_TUPLE))  # <class 'tuple'>

# parentheses is optional
MY_TUPLE = "Python",
print(type(MY_TUPLE))  # <class 'tuple'>
