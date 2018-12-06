def is_simple_check(n):
    for a in range(3, int(n/2)+1):
        if n % a == 0:
            return False
    print(n, 'is simple number')
    return True


collection = tuple(x**2+5 for x in range(1, 14))

print('Collection:', collection, type(collection), '\n')


def decor(func):
    def wrapper(*args, **kwargs):
        print('Arguments for {0} function: {1}'.format(func.__name__, (args, kwargs)))
        res = func(*args, **kwargs)
        print('RESULT =>', res, '\n')
        return res
    return wrapper


@decor
def my_find(itm, callback_funk):
    return True if callback_funk(itm) else False


for i in collection:
    my_find(i, is_simple_check)
