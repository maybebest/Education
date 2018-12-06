"""OOP. OOP. Abstraction & Inheritance & Polymorphism 2"""

from _3_abstraction_2 import Animal


class Monkey(Animal):
    """An class represention of Monkey"""

    def eat(self, food):
        print('Monkey takes food (%s) with his hand and place it into the mouth' % food)
        super().eat(food)

    @property
    def max_food(self):
        return 2


class Elephant(Animal):
    """An class represention of Elephant"""

    def eat(self, food):
        print('Elephant bring food (%s) to it mouth using it trunk' % food)
        super().eat(food)

    @property
    def max_food(self):
        return 9


animals = [Elephant('Dendy', 5), Monkey('Jimmy', 23)]

for animal in animals:
    while animal.is_hungry:
        animal.eat('Fruit')

# (9) Elephant bring food (Fruit) to it mouth using it trunk
# (2) Monkey takes food (Fruit) with his hand and place it into the mouth
