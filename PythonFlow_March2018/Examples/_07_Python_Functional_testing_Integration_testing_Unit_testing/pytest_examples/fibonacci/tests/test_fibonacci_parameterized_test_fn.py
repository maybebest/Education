"""Fibonacci fn Test. Parametrized"""

import pytest
from .. import fib


@pytest.mark.parametrize("fibonacci_limit", [9000, 100500, 1000000])
def test_fibonacci_number_25_less_than_limit(fibonacci_limit):
    assert fib(25) < fibonacci_limit

@pytest.mark.parametrize("fibonacci_limit", [9000, 100500, 1000000])
def test_fibonacci_out_of_range(fibonacci_limit):
    assert fib(30) == None, 'None should be returned.' + \
        'Fibonacci number should not be gt ' + str(fibonacci_limit)

