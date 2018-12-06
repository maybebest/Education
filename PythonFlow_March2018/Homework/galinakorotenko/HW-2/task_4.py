"""
Implement _print decorator. Decorator should print result of the decorated function evaluation
Decorate _find fn with this decorator.
Filtered items should be print automatically
"""


def my_decorator(func):
    """it Decorates returned values in function after call"""
    def wrapper(*args):
        print("\n Initial data:", *args)
        result = func(*args)
        print("\n Result we received:", str(result))
        return result
    return wrapper


my_menu = {'soup': 12, 'sandwich': 20, 'coffee': 7, 'spaghetti': 14, 'pizza': 26}


def menu_search(word):
    return word == 'spaghetti'


@my_decorator
def price_search(given_dict, func):
    return next(given_dict.get(elem) for elem in given_dict if func(elem))


price = price_search(my_menu, menu_search)
