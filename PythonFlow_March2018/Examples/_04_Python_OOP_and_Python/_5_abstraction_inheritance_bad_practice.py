"""OOP. Bad practice"""

from _1_abstraction import Animal


class Monkey(Animal):
    """An class represention of Monkey"""

    def eat(self, food):
        print('Monkey takes food (%s) with his hand and place it into the mouth' % food)
        self._Animal__append_food(food)


monkey = Monkey('Monty', 19)

monkey.eat('Fruit')
#  Monkey takes food (Fruit) with his hand and place it into the mouth
