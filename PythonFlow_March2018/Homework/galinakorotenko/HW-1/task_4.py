"""
  Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden.
"""


def word_check(a):
    if a == 'spaghetti':
        return True


def check_menu(func, menu):
    for elem in menu:
        if func(elem):
            break
    return elem


my_menu = {'soup': 12, 'sandwich': 20, 'coffee': 7, 'spaghetti': 14, 'pizza': 26}

''' SZ
    I expect that function returns found element but without return statement it returns None.
    Please add return statement to check_menu

    found_element = check_menu(word_check, my_menu)
    print(found_element) # None
'''

check = check_menu(word_check, my_menu)
print(check)
