def my_map(some_list, some_function):
    result = []
    for i in some_list:
        result.append(some_function(i))
    return result

def sqr(n):
    return n ** 2

NUMBERS = [1, 2, 3, 4, 5]

print(my_map(NUMBERS, sqr))
