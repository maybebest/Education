"""Type. Custom Metaclass"""

import unittest

def has_value(value):
    return bool(value)

class MyBadTests(unittest.TestCase):
    """Bad tests"""
    def test_all(self):
        for x in ({}, '', set(), [], False):
            self.assertEqual(has_value(x), False)

class MyTests(unittest.TestCase):
    """Usual tests"""
    def test_dictionary_has_value(self):
        test_value = {}
        self.assertEqual(has_value(test_value), False)
    
    def test_empty_string_has_value(self):
        test_value = ''
        self.assertEqual(has_value(test_value), False)

    def test_other_has_value(self):
        pass

"""To many boiler plate code! Lets use metaclass to generate tests!"""

class HasValueTestsMeta(type):
    def __new__(cls, name, bases, attrs):
        for x in ({}, '', set(), [], False):
            attrs['test_has_value_%s' % x] = cls.gen(x)

        return super().__new__(cls, name, bases, attrs)

    @classmethod
    def gen(cls, x):
        def test_fn(self):
            self.assertEqual(has_value(x), False)
        return test_fn

class MyMetaTests(unittest.TestCase, metaclass=HasValueTestsMeta):    
    pass