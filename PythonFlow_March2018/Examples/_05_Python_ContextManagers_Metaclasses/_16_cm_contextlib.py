"""Context Manager with contextlib"""

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()

with open_file('test_file') as file:
    file.write('foo')

print(file.closed)  # True