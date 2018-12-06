## Homework 7 ##
# - All functionality from HW1(functions, classes, etc.) should be covered by tests.
#   Use built-in Python's Unittest framework
# - All functionality from HW4(functions, classes, etc.) should be covered by tests.
#   Use Pytest framework
# - All scenarios should be described in test cases (positive, negative, etc.)
# - Enjoy!


import unittest
from hw1 import _find
from hw1 import _unique
from hw1 import _map
from hw1 import _filter


class TestUnitTest(unittest.TestCase):

    '''AM 
    Please use setUp method for test data. 
    "array" list could be changed during the test but each test should have initial data
    '''
    array = [1, 2, 3, 2, 4, 5, 5, 6, 7]

    def double(self, x):
        return x * 2

    def test_find(self):
        '''AM
        Tautology here. please rewrite import statement
        from hw1._find import _find, equals_five
        ...
        self.assertEquals(_find(equals_five, self.array), 5,
                          self._testMethodName)
        '''
        self.assertEquals(_find._find(_find.equals_five, self.array), 5,
                          self._testMethodName)

    @unittest.expectedFailure
    def test_find_negative(self):
        self.assertEquals(_find._find(_find.equals_five, self.array), 4,
                          self._testMethodName)

    def test_map(self):
        self.assertEquals(_map._map(self.array, self.double),
                          [2, 4, 6, 4, 8, 10, 10, 12, 14],
                          self._testMethodName)

    @unittest.expectedFailure
    def test_map_negative(self):
        self.assertEquals(_map._map(self.array, self.double),
                          [1, 3, 6, 4, 8, 0, 0, 9, 10],
                          self._testMethodName)

    def test_unique(self):
        self.assertEquals(_unique._unique(self.array), [1, 2, 3, 4, 5, 6, 7],
                          self._testMethodName)

    '''AM
    [pylint] E0102:method already defined line 55
    '''
    @unittest.expectedFailure
    def test_unique(self):
        self.assertEquals(_unique._unique(self.array), [1, 1, 3, 7, 5, 3, 7],
                          self._testMethodName)

    def test_filter(self):
        self.assertEquals(_filter._filter(_filter.is_odd_number, self.array),
                          [2, 2, 4, 6],
                          self._testMethodName)

    '''AM
    [pylint] E0102:method already defined line 67
    '''
    @unittest.expectedFailure
    def test_filter(self):
        self.assertEquals(_filter._filter(_filter.is_odd_number, self.array),
                          [2, 5, 1, 6],
                          self._testMethodName)
