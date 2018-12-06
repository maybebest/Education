"""Fibonacci fn Test"""

import unittest
from . import fib

class FibonacciTestCase(unittest.TestCase):
    """Tests for `fib`."""

    @classmethod
    def setUpClass(cls):
        """test fixture. called before each test case"""
        cls.limit = 100500 

    def test_fibonacci_number_25_less_than_limit(self):
        self.assertLess(fib(25), self.limit)

    def test_fibonacci_out_of_range(self):
        self.assertEqual(fib(30), None, 'Fibonacci number should be less then 100500')
