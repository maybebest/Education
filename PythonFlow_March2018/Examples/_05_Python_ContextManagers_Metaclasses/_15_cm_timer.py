"""Context Manager Timer Example"""
from _10_context_manager import IContextManager
import time

def fibonacci(number):    
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)

class Timer(IContextManager):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print("%s took: %0.3f seconds" % (self.name, self.interval))
        return False
   
with Timer('Calculating Fibonacci number(35)'):
    print(fibonacci(36))

# 9227465
# Calculating Fibonacci number(35) took: 3.279 seconds

