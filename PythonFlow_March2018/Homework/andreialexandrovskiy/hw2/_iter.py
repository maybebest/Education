# - Create an iterator for tuple which is created using comprehension
#   print values using: next, loop

def generate_tuple(limit):
    ''' SZ 
        Extra conversion. At first you create a list then you convert it to tuple
    '''

    ''' SZ 2 Comment not fixed '''

    return tuple([x+1 for x in range(limit)])

def iterate_tuple(tup):
    ''' SZ
        Please use iter function instead of loop and yield in purpose to create a generator
    '''

    ''' SZ 2 Comment not fixed '''

    for item in tup:
        yield item

print (next(iterate_tuple(generate_tuple(10))))
