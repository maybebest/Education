def more_than_3(n):
    return n > 3

def my_filter(some_function, some_list):
    result = []
    for i in some_list:
        if some_function(i):
            result.append(i)
    return result

NUMBERS = [1, 2, 3, 4, 5]

print(my_filter(more_than_3, NUMBERS))