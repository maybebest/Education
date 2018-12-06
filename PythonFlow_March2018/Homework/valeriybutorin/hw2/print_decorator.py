from Homework.valeriybutorin.test_data.test_data import list_to_test
from Homework.valeriybutorin.utils.utils import is_odd

"""
- Implement _print decorator. Decorator should print result of the decorated function evaluation
  Decorate _find fn with this decorator.
  Filtered items should be print automatically
- Enjoy!
"""


def print_decorator(func):
    def wrapped(*args, **kwargs):
        print("\r\nargs: {0} \r\nkwargs:{1}".format(args, kwargs))
        return func(*args, **kwargs)

    return wrapped


@print_decorator
def find_odd(func, number):
    if func(number):
        return number


print("Filter items are:", [number for number in list_to_test if find_odd(is_odd, number)])
