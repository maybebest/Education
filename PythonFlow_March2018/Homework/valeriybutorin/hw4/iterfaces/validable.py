from abc import ABC, abstractmethod

from Homework.valeriybutorin.hw4.entities.contact import Contact

'''AM (not for rework)
Validatable :)
'''
class Validable(ABC):

    @abstractmethod
    def validate(self, contact: Contact):
        pass
