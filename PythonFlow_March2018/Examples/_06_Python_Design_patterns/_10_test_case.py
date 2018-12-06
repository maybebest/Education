"""Facade Pattern example"""


class TestCase(object):
    def __init__(self, name, trigger_error=False):
        self.name, self.trigger_error = name, trigger_error

    def __setup(self):
        print('Test case %s: setup' % self.name)

    def __run(self):
        print('Test case %s: run' % self.name)

    def __complete(self, success=True):
        if success:
            print('Test case %s: complete' % self.name)
        else:
            print('Test case %s: failed' % self.name)
        return success

    def run(self):
        self.__setup()
        self.__run()
        if self.trigger_error:
            return self.__complete(False)
        return self.__complete()
