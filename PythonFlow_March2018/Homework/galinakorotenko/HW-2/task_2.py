"""
Implement your own _find function using generator expression.
first arg is callback, second arg - collection.
function returns first item from collection for which callback function call return true
generator expression usage required.
"""

my_menu = {'soup': 12, 'sandwich': 20, 'coffee': 7, 'spaghetti': 14, 'pizza': 26}


def menu_search(word):
    return word == 'spaghetti'


def price_search(given_dict, func):
    return next(given_dict.get(elem) for elem in given_dict if func(elem))


price = price_search(my_menu, menu_search)

print("New spaghetti price is", str(price))



