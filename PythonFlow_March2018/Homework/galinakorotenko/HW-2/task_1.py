"""
Implement generator function which returns filtered items of the given list (lazy _filter, items by request)
print values using: next, loop
"""

my_list = [1, 4, 6, 4, 7, 8, 8, 4]


def check_elem(i):
    return i if i % 4 == 0 else False


def _lazy_filter(given_list, callback):
    for param in given_list:
        if callback(param):
            yield param


filtered = _lazy_filter(my_list, check_elem)

for elem in filtered:
    print(elem)







