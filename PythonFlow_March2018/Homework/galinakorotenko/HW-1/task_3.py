"""
  Implement your own _map function.
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.
"""


def my_func(i):
    i = i+1
    return i


def my_map(func, data_list):
    new_list = []
    for elem in data_list:
        new_list.append(func(elem))
    return new_list


my_list = [2, 3, 4, 5, 6, 7]


print(my_map(my_func, my_list))
