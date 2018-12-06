"""
Module with all utils
"""


def is_int(item):
    """:return True if item type is int"""
    '''AM (not for rework)
    standard isinstance functions could be used here
    VB - done,
    Question: should I use standard libs or better to impalement own function?
    '''
    return isinstance(item, int)


def is_odd(number):
    """:return True if number is odd"""
    if is_int(number) and odd_filter(number):
        return True


def map_to_string(item):
    """:return collection where all items are str"""
    return str(item)


def odd_filter(number):
    """:return collection where all items are str"""
    return number if is_int(number) and not number % 2 == 0 else None


def to_type(expected_type, collection):
    """:return expected type of the collection"""
    return type(expected_type)(collection)
