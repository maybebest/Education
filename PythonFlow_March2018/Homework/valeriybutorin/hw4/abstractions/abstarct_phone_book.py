from abc import abstractmethod, ABC, abstractproperty

from Homework.valeriybutorin.hw4.entities.contact import Contact

'''AM (not for rework)
I think considering this class as an interface would be more suitable here:
f.e. IPhoneBook
'''
class AbstractPhoneBook(ABC):
    @abstractmethod
    def remove_contact(self, contact: Contact):
        pass

    @abstractmethod
    def add_contact(self, contact: Contact):
        pass

    @abstractmethod
    def find_contact(self, contact: Contact, full_name):
        pass

    @abstractproperty
    def favorites(self):
        pass
