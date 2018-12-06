"""Context Manager with contextlib"""

from contextlib import contextmanager
import time

@contextmanager
def Timer(name):
    start = time.time()
    yield 
    end = time.time()    
    print("%s took: %0.3f seconds" % (name, end - start))

def fibonacci(number):    
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)

with Timer('Calculating Fibonacci number(35)'):
    print(fibonacci(35))

# 9227465
# Calculating Fibonacci number(35) took: 3.237 seconds
