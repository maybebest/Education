

"""O(N^2) represents an algorithm whose performance is directly proportional
to the square of the size of the input data set. This is common with algorithms
that involve nested iterations over the data set.
Deeper nested iterations will result in O(N3), O(N4) etc..
"""

i = 0
def contains_duplicates(elements):
    """Return True if elements contains value, otherwise return false"""
    for outer in elements:
        for inner in elements:
            global i
            i += 1
            # Don't compare with self
            if (outer == inner):
                continue
            if elements[outer] == elements[inner]:
                return True
    return False


my_list = list(range(1024))
print('Has duplicates: %s; Operations: %s' %
      (contains_duplicates(my_list), i))

# Has duplicates: False; Operations: 1048576


