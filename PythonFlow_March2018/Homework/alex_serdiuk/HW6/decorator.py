"""## Homework 6 ##
- Implement Decorator(pattern, not Python Decorator) to decorate some instance of some class with some functionality
- Read about more patterns!
- Enjoy!"""


class power(object):
    def action_one(self):
        print("hello")
    def action_two(self):
        print("let`s go")

'''AM
[pylint] C0103:Class name "power_decorator" doesn't conform to PascalCase naming style
'''
class power_decorator(object):
    def __init__(self, message):
        self._message = message
    def action_one(self):
        print("decorated action_one")
        self._message.action_one()
    def __getattr__(self, name):
        return getattr(self._message, name)

o = power()
p = power_decorator(o)
p.action_one()
p.action_two()



