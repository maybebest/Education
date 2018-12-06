# - Implement your own _find function using generator expression.
#   first arg is callback, second arg - collection.
#   function returns first item from collection for which callback function call return true
#   generator expression usage is required.

def coll_gen(start, end):
    return tuple(range(start, end))

def divisable_by_five(x):
    return (x % 5) == 0

def _find(func, coll):
    ''' SZ
    Please use generator expression here:

    def _find(func, coll): 
        return next((<<your generator expression here>>), None)
    '''

    ''' SZ 2 comment not fixed '''
    
    for item in coll:
        if func(item):
            return item

print (_find(divisable_by_five, coll_gen(12, 47)))
