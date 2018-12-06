"""Facade Pattern example"""

from _10_test_case import TestCase


class TestRunner(object):
    __tests = []
    __result = None

    def __init__(self, test_cases):
        self.__tests.extend(test_cases)

    def run_all(self):
        self.__result = [t.run() for t in self.__tests]

    def create_report(self):
        # here may be usage of reporter class
        print(self.__result)

    @property
    def success(self):
        return all(self.__result)


if __name__ == '__main__':
    test_runner = TestRunner([TestCase('Test1'), TestCase('Test2', True)])
    test_runner.run_all()
    test_runner.create_report()

    assert test_runner.success
