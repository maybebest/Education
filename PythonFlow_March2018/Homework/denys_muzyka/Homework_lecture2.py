# def sqr(number):
#     return number ** 2
my_list = [1, 2, 3, 4, 3, 2, 1]


"""Lazy filter"""

def module_by(x):
    if x % 2 == 0:
        return x
    return False

def my_lazy_f(callback, my_list):
    '''SZ (not for rework)
        It could be implemented more elegant with inline generator expression

        return (item for item in my_list if callback(item))
    '''
    for some in my_list:
        if callback(some):
            yield some
# python_go = my_lazy_f(lambda n: n % 2 != 0, [1,2,3,4])
python_go = my_lazy_f(module_by, my_list)
print(next(python_go))
print(next(python_go))


"""My find through Generator + Decorator"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call", *args, **kwargs)
        result = func(*args, **kwargs)
        print("After call", result)
        return result
    return wrapper

def check_callback(value):
    if value > 2:
        return True
    return False

@my_decorator
def my_find(collection, callback_func):
    ''' SZ (not for rework)
        Why didn't you use expression like this at my_lazy_f function?
    '''
    gen = (some for some in collection if callback_func(some))
    # for i in col:
    #     if callback_func(i):
    #         return i
    return next(gen)

print(my_find(my_list, check_callback))



"""Iterator """

my_comp = tuple(x**2 for x in range(10))
itr = iter(my_comp)

for some in range(len(my_comp)):
    print(some+1, 'next =>', next(itr))



