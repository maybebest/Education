from Homework.bohdankrainov.HW1.file import collection, filter_check

print('===HW2===')
print(collection)


'''AM
1)
_lazy_f function should take callback and collection as args (like in first HW)
2)
Why do you use "while True" here? It could be written simplier\
def lazy_filter(cb, collection):
    for el in collection:
        if cb(el):
            yield el

gen = lazy_filter(lambda n: n % 2 != 0, [1,2])
print(next(gen)) # 1
'''


def _lazy_f(callback_func, col):
    for el in col:
        if callback_func(el):
            print('next =>', el)
            yield el
            print('current in next:', el)


"""
def filter_check(i):
    if i % 8 == 0:
        return i
"""

lf = _lazy_f(filter_check, collection)

for n in range(4):
    print(n+1, 'lazy filter call ->', next(lf))
