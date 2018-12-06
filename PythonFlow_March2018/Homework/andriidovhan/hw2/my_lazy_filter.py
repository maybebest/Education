def more_than_3(n):
    return n > 3

'''AM
In this implementation filter is not lazy
All results returned by function call 
my_lazy_filter(more_than_3, NUMBERS)
but we need lazy filter so the function should return iterator or generator
i believe generator expression could be used here
'''

"""# before:
def my_lazy_filter(some_function, some_list):
     return list(n for n in some_list if some_function(n))
NUMBERS = [1, 2, 7, 3, 4, 5, 6]
test_iter=iter(my_lazy_filter(more_than_3, NUMBERS))
print(next(test_iter))
print(next(test_iter))
"""
# after:    
def my_filter(some_function, some_list):
    for i in some_list:
        if some_function(i):
            yield i

NUMBERS = [1, 2, 7, 3, 4, 5, 6]
TEST_ITER = my_filter(more_than_3, NUMBERS)
print(next(TEST_ITER))
print(next(TEST_ITER))
