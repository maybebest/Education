"""OOP. Abstraction 2"""
from abc import ABC, abstractmethod, abstractproperty


class Animal(ABC):
    """An abstract class represention of Animal"""

    def __init__(self, name, age):
        self.__food, self.name, self.age = [], name, age

    @abstractmethod
    def eat(self, food):
        self.__append_food(food)

    def __append_food(self, food):
        if len(self.__food) < self.max_food:
            self.__food.append(food)

    @property
    def is_hungry(self):
        return len(self.__food) != self.max_food

    @abstractproperty
    def max_food(self): pass

#  animal = Animal('Monkey', 23)
#  TypeError: Can't instantiate abstract class Animal with abstract methods eat
