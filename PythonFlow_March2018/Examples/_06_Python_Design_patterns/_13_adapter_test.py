"""Adapter Pattern example"""

from _10_test_case import TestCase
from _12_test_suite import TestSuite
from _11_facade_test_runner import TestRunner

class TestAdapter(object):
    def __init__(self, test, **adapted_methods):
        self.test = test
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.test, attr)

test = TestCase('Test1')
suite = TestSuite([TestCase('Test2'), TestCase('Test3', True)])

all_tests = [TestAdapter(test,  run=test.run),
             TestAdapter(suite, run=suite.run_suit)]

test_runner = TestRunner(all_tests)
test_runner.run_all()

assert test_runner.success
