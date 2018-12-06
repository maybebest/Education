# - Implement generator function which returns filtered items of the
#   given list (lazy _filter, items by request)
#   print values using 'next' loop


def divisable_by_three(x):
    return (x % 3) == 0


gen = (x for x in range(10, 35))
print(type(gen))


def _filter(func, coll):
    ''' SZ This works as well but task means that filter function
        receives 2 arguments - callback and collection. You need to iterate through that collection
        and yield an item if callback returns true '''
        
    '''AM
    Why do you use next here?
    I see two simlier way to resolve the task:
    1)
    def lazy_filter(cb, collection):
        for el in collection:
            if cb(el):
                yield el

    gen = lazy_filter(lambda n: n % 2 != 0, [1,2])
    print(next(gen)) # 1
    2)
    def lazy_filter(cb, coll):
        return (i for i in coll if cb(i))
    
    gen = lazy_filter(lambda n: n % 2 != 0, [1,2])
    print(next(gen)) # 1
    '''
    yield next(i for i in coll if func(i))


for i in range(7):
    print (next(_filter(divisable_by_three, gen)))
