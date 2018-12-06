"""Fibonacci fn Test"""

from .. import fib

def setup_module(module):
    global limit
    limit = 100500

def test_fibonacci_number_25_less_than_limit():
    assert fib(25) < limit

def test_fibonacci_out_of_range():
    assert fib(30) == None, 'None should be returned.' + \
        'Fibonacci number should not be gt 100500'


