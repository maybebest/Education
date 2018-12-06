"""OOP. Abstraction & Inheritance & Polymorphism 1"""

from _1_abstraction import Animal


class Monkey(Animal):
    """An class represention of Monkey"""

    def eat(self, food):
        print('Monkey takes food (%s) with his hand and place it into the mouth' % food)
        super().eat(food)


class Elephant(Animal):
    """An class represention of Elephant"""

    def eat(self, food):
        print('Elephant bring food (%s) to it mouth using it trunk' % food)
        super().eat(food)


animals = [Elephant('Dendy', 5), Monkey('Jimmy', 23)]

for animal in animals:
    if animal.is_hungry:
        animal.eat('Fruit')

# Elephant bring food (Fruit) to it mouth using it trunk
# Monkey takes food (Fruit) with his hand and place it into the mouth
