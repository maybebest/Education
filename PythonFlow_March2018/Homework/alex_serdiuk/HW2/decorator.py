
"""- Implement _print decorator. Decorator should print result of the decorated function evaluation
  Decorate _find fn with this decorator.
  Filtered items should be print automatically
- Enjoy!"""

'''SZ this decorator doesn't print any values,
    please add printing of result of target function evaluation
'''
def print_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        '''AM (not for rework)
        Extra original_function(*args, **kwargs) evaluation:
        result should be stored in var then printed then returned:
        res = original_function(*args, **kwargs)
        print("Rule", res)
        return res
        '''
        print("Rule", original_function(*args, **kwargs))
        return original_function(*args, **kwargs)
    return wrapper_function

@print_decorator
def dop(n):
    return n >= 3

@print_decorator
def my_find(callback, collection):
    for item in collection:
        if callback(item) == True:
            return item

test_data = [1, 2, 3, 3, 4, 5, 5, 9, 7, 2, 3]

my_find(dop, test_data)