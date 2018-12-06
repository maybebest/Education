"""OOP. Bad practice"""
from _1_abstraction import Animal


class Monkey(Animal):
    """An class represention of Monkey"""

    def eat(self, food):
        print('Monkey takes food (%s) with his hand and place it into the mouth' % food)
        super().eat(food)

    def _Animal__append_food(self, food):
        print('Monkey: Is hungry (%s)...' % self.is_hungry)


class FunnyMonkey(Monkey):

    def _Animal__append_food(self, food):
        print('FunnyMonkey: Is hungry (%s)...' % self.is_hungry)


funny_monkey, monkey = FunnyMonkey('Jimmy', 23), Monkey('Monty', 19)

monkey.eat('Fruit')
#  Monkey takes food (Fruit) with his hand and place it into the mouth
#  Monkey: Is hungry (True)...
funny_monkey.eat('Fruit')
#  Monkey takes food (Fruit) with his hand and place it into the mouth
#  FunnyMonkey: Is hungry (True)...
