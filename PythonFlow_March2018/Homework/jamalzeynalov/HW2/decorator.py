"""
- Implement _print decorator. Decorator should print result of the decorated function evaluation
  Decorate _find fn with this decorator.
  Filtered items should be print automatically
- Enjoy!
"""


def my_print(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Result is: %s" % result)
        return result

    return wrapper
