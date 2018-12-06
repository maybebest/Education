"""List"""

MY_LIST = []
MY_LIST = [1, 2, 3]
MY_LIST = [1, "Hello", 3.4]

# nested list
MY_LIST = ["mouse", [8, 4, 6], ['a']]
print(MY_LIST)  # ['mouse', [8, 4, 6], ['a']]

# access to elements
print(MY_LIST[1])      # [8, 4, 6]
print(MY_LIST[-1][0])  # a
print(MY_LIST[1.0])    # TypeError: list indices must be integers or slices, not float
