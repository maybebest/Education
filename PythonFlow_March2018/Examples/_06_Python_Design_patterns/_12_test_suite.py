"""Adapter Pattern example"""


class TestSuite(object):
    def __init__(self, test_cases):
        self.__tests = test_cases

    def run_suit(self):
        return all([self.run(t) for t in self.__tests])

    def run(self, test):
        self.before_each(test)
        result = test.run()
        self.after_each(test)
        return result

    def before_each(self, test):
        print('Before %s' % test.name)

    def after_each(self, test):
        print('After %s' % test.name)
