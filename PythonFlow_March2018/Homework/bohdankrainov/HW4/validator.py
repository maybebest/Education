from Homework.bohdankrainov.HW4.contacts import IContact
from abc import ABC, abstractmethod
import re


class IValidator(ABC):

    @abstractmethod
    def validate(self, item):
        pass


class Validator(IValidator):

    def __init__(self, pattern):
        self.pattern = pattern

    def validate(self, contact):
        return True if re.match(self.pattern, contact.phone) is not None else False
