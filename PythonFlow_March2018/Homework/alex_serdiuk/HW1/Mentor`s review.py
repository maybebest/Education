__author__ = 'aserdiuk2'

'''AM 
Requirements are not implemented:
- Implement your own _uniq function.
- Implement your own _filter function.
- Implement your own _map function.
- Implement your own _find function.

You should implement/realize you own functions _uniq, _filter, _map, _find
I should be able to use your functions in the same way as i use standard built-in functions

def _filter(callback, collection):

    """Your implementation of standard filter function should be here"""
    pass
list(filter(lambda x: x > 1, [1,2,3])) == [2,3]
_filter(lambda x: x > 1, [1,2,3]) == [2,3]
##################################

def _find(callback, collection):
    """Your implementation of find function should be here"""
    pass
_find(lambda x: x > 1, [1,3,2]) == 3
###################################

def _uniq(collection):
    """Your implementation of uniq function should be here"""
    pass
_uniq([1,3,3,2]) == [1,3,2]
###################################

def _map(callback, collection):
    """Your implementation of map function should be here"""
    pass
_map(lambda x: x - 1, [1,3,2]) == [0, 2, 1]
'''

'''AM
[pylint] W0621:Redefining name 'l' from outer scope (line 8)
Please don't use global variables names as variable names inside function
This is a bad practice.
Also this is a quite strange function, what is "l.append(15)"?
'''

