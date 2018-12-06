"""
- Implement Decorator(pattern, not Python Decorator) to decorate some instance of some class with some functionality
"""

"""Decorator Pattern example"""


def open_bottle(cl):
    setattr(cl, 'is_open', True)
    return cl


class MilkBottle(object):
    def __init__(self, fat, lactose):
        self.fat = fat
        self.lactose = lactose


milk_bottle = MilkBottle(5, 2)

open_bottle(milk_bottle)

if hasattr(milk_bottle, 'is_open'):
    print(milk_bottle.is_open)
