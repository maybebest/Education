"""
  Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden.
"""


def check_value(a):
    ''' SZ (not for rework)
        It is possible to simplify this function like this
        return a > 5
    '''
    if a > 5:
        return True


def new_filter_function(func, data_list):
    new_list = []
    for item in data_list:
        if func(item):
            new_list.append(item)
    return new_list


my_list = [1, 4, 6, 4, 7, 8, 8, 4]


new_values = new_filter_function(check_value, my_list)
print(new_values)

