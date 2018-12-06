"""
- Implement _print decorator. Decorator should print result of the decorated function evaluation
  Decorate _find fn with this decorator.
  Filtered items should be printed automatically
"""
lst = ['Jack', 27, 'USA', 5, "Jack", 'New York', 27, 44, 44]

def reporter(func):
    def details(*args, **kwargs):
        ''' SZ 
            Decorator function should returns a value that was returned by the target function.
            Now after decoration _ find function returns None instead of search result
        '''
        ''' SZ This is not requirement but we use Python 3 :) '''

        ''' SZ 2 Comment not fixed '''
        
        print "Found results: ", func(*args, **kwargs)
    return details

def equals_five(x):
    return x == 5

@reporter
def _find(func, collect):
    for i in collect:
        if func(i):
            return i

_find(equals_five, lst)
