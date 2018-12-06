"""Manipulations with classes"""

class Foo(object):
    pass

foo = Foo

def choose_class(name, foo):
    if name == 'foo':
        return foo
    else:
        class Bar(object):
            pass
        return Bar

instance = choose_class('foo', foo)()



