"""OOP. Abstraction 1"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract class represention of Animal"""
    name = None
    age = None

    def __init__(self, name, age):
        self.name, self.age = name, age
        self.__food = []

    @abstractmethod
    def eat(self, food):
        self.__append_food(food)

    def __append_food(self, food):
        self.__food.append(food)

    @property
    def is_hungry(self):
        return len(self.__food) == 0

#  animal = Animal('Monkey', 23)
#  TypeError: Can't instantiate abstract class Animal with abstract methods eat
