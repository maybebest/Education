'''
- Implement _print decorator. Decorator should print result of the decorated function evaluation
  Decorate _find fn with this decorator.
  Filtered items should be print automatically
'''


def my_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("My Odd Numbers List:\n", result)
        return result

    return wrapper


@my_decorator
def _find_odd(collection):
    new_collection = []
    for item in collection:
        if item % 2 == 0 and item != 0:
            new_collection.append(item)
    return new_collection


my_collection = range(0, 21)
_find_odd((list(my_collection)))

