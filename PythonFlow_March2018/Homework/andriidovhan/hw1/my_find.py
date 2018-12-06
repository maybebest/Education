def less_than_3(n):
    return n < 3

def my_find(some_function, some_list):
    for i in some_list:
        if some_function(i):
            return i

NUMBERS = [8, 3, 3, 2, 5]

print(my_find(less_than_3, NUMBERS))