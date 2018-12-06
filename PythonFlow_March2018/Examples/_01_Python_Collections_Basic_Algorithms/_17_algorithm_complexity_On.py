"""O(N) describes an algorithm whose performance will grow linearly
and in direct proportion to the size of the input data set.

The example below also demonstrates how Big O favours the worst-case
performance scenario;

A matching string could be found during any
iteration of the for loop and the function would return early,
but Big O notation will always assume the upper limit where the
algorithm will perform the maximum number of iterations.
"""

def contains_value(elements, value):
    """Return True if elements contains value, otherwise return false"""
    for element in elements:
        if element == value:
            return True
    return False


my_list = list(range(50))
print(contains_value(my_list, 51))  # False
print(contains_value(my_list, 1))  # True

