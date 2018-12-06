"""Decorators"""


def my_decorator(func):
    """Decorate input function with logs before and after call.
    return new decorated function"""
    def wrapper(*args, **kwargs):
        print("Before call", *args, **kwargs)
        result = func(*args, **kwargs)
        print("After call", result)
        return result

    return wrapper


@my_decorator
def add(a, b):
    "Our add function"
    return a + b


add(1, 3)
# Before call 1 3
# After call 4
