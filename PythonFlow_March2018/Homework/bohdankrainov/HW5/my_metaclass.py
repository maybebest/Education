import random
import unittest


def is_prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True


class MyMetaClass(type):

    def __new__(mcs, name, bases, attrs):
        rand_list = random.sample(range(3, 37, 2), 5)
        print('List:', rand_list)
        for i in rand_list:
            attrs['test_{0}_is_prime'.format(i)] = mcs.gen(i)
        return super().__new__(mcs, name, bases, attrs)

    @classmethod
    def gen(mcs, i):
        def test_fn(self):
            self.assertEqual(is_prime(i), True)
        return test_fn

    # def __call__(cls):
    #     print(cls.__dict__)
    #     unittest.main(cls)


class MyTestClass(unittest.TestCase, metaclass=MyMetaClass):
    pass


a = MyTestClass()
unittest.main(a, verbosity=2)

