
# import unittest

# class TestSomeFunctionality(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print('setup class')

#     def setUp(self):
#         print('setup method')
    
#     def test_five_bigger_then_four(self):
#         print('TEST')
#         self.assertGreater(5, 4, 'Assertion message')

#     def test_five_less_then_six(self):
#         print('TEST')
#         self.assertLess(5, 6, 'Assertion message')

#     def tearDown(self):
#         print('teardown method')

#     @classmethod
#     def tearDownClass(cls):
#         print('teardown class')

from pytest_examples.fibonacci.tests import test_fibonacci_out_of_range
