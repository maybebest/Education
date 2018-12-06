import unittest
import inspect
import random
from Homework.bohdankrainov.HW1 import file


class TestHW1(unittest.TestCase):

    '''AM
    Please use 'setUp' for test data (test_collection)
    Tests should be independent from each other, 
    but in your case test_collection could be changed during the tests 
    and other tests will be affected
    '''
    @classmethod
    def setUpClass(cls):
        print('\n\n<========Testing of HW1 started=======>\n')
        cls.negative_test_values = [123, True, 16.13, False]

    def setUp(self):
        self.test_collection = random.sample(range(1, 100), 20)
        # self.test_collection = [1, 2, 3, 7, 4, 5, 137, 21, 3, 27, 24, 1, 2, 4, 7, 3, 56, 5, 8, 24]

    def test_my_uniq_positive(self):
        self.assertEqual(sorted(file.my_uniq(self.test_collection)), sorted(set(self.test_collection)),
                         'my_uniq function works incorrect')

    def test_my_uniq_negative(self):
        for i in self.negative_test_values:
            try:
                file.my_uniq(i)
            except TypeError as exc:
                print(inspect.stack()[0][3], exc, exc.__class__)
                self.assertEqual(exc.args[0], "'{}' object is not iterable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_uniq function passed with {0}({1}) '
                                     'argument!'.format(i, type(i)))

    def test_my_filter_positive(self):
        self.assertEqual(file.my_filter(file.check_odd, self.test_collection),
                         list(filter(file.check_odd, self.test_collection)),
                         'my_filter functions works incorrect')

    def test_my_filter_negative(self):
        for i in self.negative_test_values:
            try:
                file.my_filter(i, self.test_collection)
            except TypeError as err:
                print(inspect.stack()[0][3], err, err.__class__)
                self.assertEqual(err.args[0], "'{}' object is not callable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_filter function passed with {0}({1}) as callback '
                                     'argument'.format(i, type(i)))

            try:
                file.my_filter(file.check_odd, i)
            except TypeError as err:
                print(inspect.stack()[0][3], err, err.__class__)
                self.assertEqual(err.args[0], "'{}' object is not iterable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_filter function passed with {0}({1}) as collection '
                                     'argument'.format(i, type(i)))

    def test_my_map_positive(self):
        self.assertEqual(list(map(lambda x: x**2, self.test_collection)),
                         file.my_map(lambda x: x**2, self.test_collection), 'my_map function works incorrect')

    def test_my_map_negative(self):
        for i in self.negative_test_values:
            try:
                file.my_map(i, self.test_collection)
            except TypeError as err:
                print(inspect.stack()[0][3], err, err.__class__)
                self.assertEqual(err.args[0], "'{}' object is not callable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_map function passed with {0}({1}) as callback '
                                     'argument'.format(i, type(i)))

            try:
                file.my_filter(lambda x: x*3, i)
            except TypeError as err:
                print(inspect.stack()[0][3], err, err.__class__)
                self.assertEqual(err.args[0], "'{}' object is not iterable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_map function passed with {0}({1}) as collection '
                                     'argument'.format(i, type(i)))

    def test_my_find_positive(self):
        self.res = file.my_find(file.filter_check, self.test_collection)
        print(inspect.stack()[0][3], self.test_collection, self.res)
        self.assertEqual(self.res, next(iter(filter(file.filter_check, self.test_collection))),
                         'my_find function works incorrect')

    def test_my_find_negative(self):
        for i in self.negative_test_values:
            try:
                file.my_find(i, self.test_collection)
            except TypeError as err:
                print(inspect.stack()[0][3], err, err.__class__)
                self.assertEqual(err.args[0], "'{}' object is not callable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_find function passed with {0}({1}) as callback '
                                     'argument'.format(i, type(i)))

            try:
                file.my_find(file.filter_check, i)
            except TypeError as err:
                print(inspect.stack()[0][3], err, err.__class__)
                self.assertEqual(err.args[0], "'{}' object is not iterable".format(i.__class__.__name__),
                                 'Unexpected Error message')
            else:
                raise AssertionError('Negative test for my_find function passed with {0}({1}) as collection '
                                     'argument'.format(i, type(i)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
