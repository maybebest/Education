"""
- Implement PhoneBook class.
- use OOP and SOLID
- Class should be an iterable (interface).
- Class should contain methods:
  add_contact method (take object: IContact and add it to phone book)
  find_contact method (first match by name)
  remove_contact method (by name)
  add_to_favorites method (take object: IContact and add it to phone book (only if exists))
  call method (take object: IContact and print 'Calling to <contact name>...'])
  recent_calls property (returns recent calls<IContact>)
  favorites property (returns favorites contacts<IContact>)
- add_contact should check contact's number with regex(or other)validator before add it to phone book
  (one validator per phone book instance)
- Enjoy!
"""
from abc import ABC, abstractmethod
from collections import deque

import re

from Homework.jamalzeynalov.HW1.home_work_1 import my_own_find


class IIterable(ABC):
    @abstractmethod
    def __iter__(self): pass


class IValidator(ABC):
    @abstractmethod
    def validate(self, string: str): pass


class PhoneNumberValidator(IValidator):
    def __init__(self, pattern):
        self.__pattern = pattern

    def validate(self, string: str):
        return string.startswith(self.__pattern)


class PhoneNumberRegexpValidator(IValidator):
    def __init__(self, operator_code):
        """
        :param operator_code: The code the number must start with (e.g. 095)
        """
        self.__operator_code = operator_code

    def validate(self, string: str):
        res = re.search(self.__operator_code, string).group(0)
        return len(res) == len(string)


'''AM
Interfaces have no implementation, just declarations
"add_contact method (take object: IContact and add it to phone book)"
Here i meant that add_contact method could take any object which implements IContact interface
class IContact(ABC):
    @property    
    @abstractmethod
    def name(self): pass

    @property
    @abstractmethod
    def phone(self): pass

class PhoneBookContact(IContact):
    def __init__(self, name: str, phone: str):
        self.__name, self.__phone = str(name), str(phone)        

    def __eq__(self, other):
        return all([bool(getattr(self, f) == getattr(other, f)) for f in self.__dict__])

    def __repr__(self):
        return "<{}: {}>".format(self.name, self.phone)

    @property    
    def name(self): return self.__name

    @property
    def phone(self): return self.__phone

...
def add_contact(self, contact: IContact):

PhoneBook(CustomValidator()).add_contact(PhoneBookContact())
...

The same for validators

class IValidator(ABC):
    @abstractmethod
    def validate(self): pass

class CustomValidator(IValidator):
    def __init__(self, pattern):
        self.pattern = pattern

    def validate(self, string):
        res = re.search(self.pattern, string).group(0)
        return len(res) == len(string)

...
def __init__(self, validator: IValidator):

PhoneBook(CustomValidator())
...
'''


class IContact(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @property
    @abstractmethod
    def phone(self): pass


class PhoneBookContact(IContact):
    def __init__(self, name: str, phone: str):
        self.__name = str(name)
        self.__phone = str(phone)

    def __eq__(self, other):
        return all([bool(getattr(self, f) == getattr(other, f)) for f in self.__dict__])

    def __repr__(self):
        return "<{}: {}>".format(self.__name, self.__phone)

    @property
    def name(self): return self.__name

    @property
    def phone(self): return self.__phone


class PhoneBook(IIterable):
    def __init__(self, validator: IValidator):
        self.__phonebook = []
        self.__favorites = []
        self.__recent = deque([], maxlen=50)
        self.__validator = validator

    def __iter__(self):
        return iter(self.__phonebook)

    def __contains__(self, item: IContact):
        return bool([x for x in self.__phonebook if x == item])

    def __repr__(self):
        return str(self.__phonebook)

    @property
    def favorites(self):
        return self.__favorites

    @property
    def recent_calls(self):
        return self.__recent

    def add_contact(self, contact: IContact):
        if contact not in self:
            if self.__validator.validate(str(contact.phone)):
                self.__phonebook.append(contact)
            else:
                print("Phone number is invalid: {}".format(contact.phone))
        else:
            print("Contact {} is already in your phonebook.".format(contact))

    def find_contact(self, name):
        """ find_contact method (first match by name) """
        return my_own_find(lambda x: x.name == name, self.__phonebook, to_return=False)

    def remove_contact(self, name: str):
        contact = self.find_contact(name)
        self.__phonebook.remove(contact) if contact else print("'{}' is not in your phonebook".format(name))

    def add_to_favorites(self, contact: IContact):
        # add_to_favorites method (take object: IContact and add it to phone book (only if exists))
        if contact in self:
            self.__favorites.append(contact)
        else:
            print("'{}' is not in your phonebook. First add it.".format(contact.name))

    def call(self, contact: IContact):
        # """call method (take object: IContact and print 'Calling to <contact name>...'])"""
        if contact in self:
            print("Calling to <{}>...".format(contact.name))
            self.__recent.append(contact)
        else:
            print("Calling to <{}>...".format(contact.phone))
            self.__recent.append(contact)


ph_book = PhoneBook(PhoneNumberRegexpValidator(r'\d*'))
ph_book2 = PhoneBook(PhoneNumberValidator("095"))

she = PhoneBookContact("She", '0957788123')
he = PhoneBookContact("He", '0957788321')

ph_book.add_contact(she)
ph_book2.add_contact(he)

print(ph_book)
print(ph_book2)
