"""Fibonacci fn Test. Extended fixture"""

import pytest
from .. import fib

@pytest.fixture(scope="session", params=[9000, 100500, 1000000])
def fibonacci_limit(request):    
    return request.param

def test_fibonacci_number_25_less_than_limit(fibonacci_limit):
    assert fib(25) < fibonacci_limit

@pytest.mark.critical()
def test_fibonacci_out_of_range(fibonacci_limit):
    assert fib(30) == None, 'None should be returned.' + \
        'Fibonacci number should not be gt ' + str(fibonacci_limit)

