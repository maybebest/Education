def my_decorator(func):
    def wrapper(some_fn, some_list):
        print("some text BEFORE executing", "function: '{}' and list: {}".format(some_fn.__name__, some_list))
        result = func(some_fn, some_list)
        print("some text AFTER executing", next(result))
        return result

    return wrapper

def less_than_3(n):
    return n < 3

'''AM (not for rework)
it could be written in another way
def my_find(some_function, some_list):
    return next((n for n in some_list if some_function(n)), None)

in this case usage is more simplier:
my_find(less_than_3, NUMBERS))
'''
@my_decorator
def my_find(some_function, some_list):
    return (n for n in some_list if some_function(n))

NUMBERS = [8, 3, 3, 2, 5, 2]
print(next(my_find(less_than_3, NUMBERS)))