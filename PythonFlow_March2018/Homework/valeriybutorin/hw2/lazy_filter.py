'''AM
ModuleNotFoundError: No module named 'Homework'
Please use relative imports inside your package.
'''
from Homework.valeriybutorin.test_data.test_data import list_to_test
from Homework.valeriybutorin.utils.utils import odd_filter
"""
# The path builder from the "source" of the project where root is PythonFlow_March2018
# Alexander please provide me an example of correct relative path
"""

"""
- Implement generator function which returns filtered items of the given list (lazy _filter, items by request)
  print values using: next, loop
"""


def generator_lazy_odd(func, collection):
    for item in collection:
        if func(item):
            yield item

'''AM
1)
Generator has a bug: On each iteration i have the same output
gen = generator_lazy_odd([1,2])
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) # 1
2)
Why do you use "while True" here? It could be written simpler\
def lazy_filter(cb, collection):
    for el in collection:
        if cb(el):
            yield el

gen = lazy_filter(lambda n: n % 2 != 0, [1,2])
print(next(gen)) # 1
'''

lazy_odd_generator_instance = generator_lazy_odd(odd_filter, list_to_test)

print("Print value by next: ", next(lazy_odd_generator_instance))
print("Print value in loop: ", [number for number in lazy_odd_generator_instance])
