"""
- Implement Facade pattern for some classes (up to you) (try not to use code from examples :) )
  Especially for Valera: subject - Animals :)
"""


# Complex parts
class Tiger(object):
    @staticmethod
    def eat(food): print("{0} eating: {1}".format(__class__.__name__, food))


class Wolf(object):
    @staticmethod
    def eat(food): print("{0} eating: {1}".format(__class__.__name__, food))


class Lion(object):
    @staticmethod
    def eat(food): print("{0} eating: {1}".format(__class__.__name__, food))


class Zoo(object):
    def __init__(self):
        self.tiger = Tiger()
        self.wolf = Wolf()
        self.lion = Lion()

    def breakfast(self):
        self.tiger.eat("chicken")
        self.wolf.eat("rabbit")
        self.lion.eat("pig")


Zoo().breakfast()
