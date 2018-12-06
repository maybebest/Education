"""Fibonacci fn Test. Extended fixture"""

import pytest
from .. import fib

@pytest.fixture(scope="session")
def fibonacci_limit_resource():    
    file = open('fibonacci_limit')
    yield file
    file.close()

@pytest.fixture(scope="function")
def fibonacci_limit(fibonacci_limit_resource):   
    limit = fibonacci_limit_resource.read()
    fibonacci_limit_resource.seek(0)
    return int(limit)

def test_fibonacci_number_25_less_than_limit(fibonacci_limit):
    assert fib(25) < fibonacci_limit

def test_fibonacci_out_of_range(fibonacci_limit):
    assert fib(30) == None, 'None should be returned.' + \
        'Fibonacci number should not be gt ' + str(fibonacci_limit)

