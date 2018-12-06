'''
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
'''

import re

from abc import ABC, abstractmethod

'''AM
Usually interfaces don't contain constructor
Also here i see that you define method name, method number an then you are redefine these methods in the constructor
Also interface should have empty abstract methods and should be derived from ABC class
Please use this example to rework your interface:
from abc import ABC, abstractmethod

class IContact(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @property
    @abstractmethod
    def number(self): pass
'''
class IContact(object):

    def name(self): pass

    def number(self): pass

    def __init__(self, name, number):
        self.name = name
        self.number = number


class PhoneBook(IContact):

    # @property
    # def __sizeof__(self): pass
    #
    # @__sizeof__.setter
    # def __sizeof__(self, val): self.__sizeof__ = val
    #
    # @__sizeof__.getter
    # def __sizeof__(self):
    #     return self.__sizeof__

    '''AM
    "recent_calls property (returns recent calls<IContact>)"
    "favorites property (returns favorites contacts<IContact>)"

    recent_calls and favorites should be class properties (methods with @property decorator)
    '''
    def __init__(self):
        self.contacts = {}
        self.favorites = {}
        self.recent_calls = {}

    def __iter__(self):
        '''AM
        [pylint] E1101:Instance of 'PhoneBook' has no '__contacts' member
        please use self.contacts here
        '''
        return iter(self.contacts)

    def add_contact(self, cont: IContact):
        '''AM
        Please 
        1) make new class RegexValidator which implements interface IValidator (interface has one abstract method "validate")
        2) RegexValidator class instance should be passed to PhoneBook class constructor and remembered in variable
        3) Use remembered in constructor validator here to validate phone number
        '''
        try:
            match = re.match("^[0-9]+$", cont.number)
            if match:
                '''AM
                Please save hole  cont object to contacts dictionary
                '''
                self.contacts[cont.name] = cont.number
            else:
                raise KeyError("Digits are expected as a phone number")
        except KeyError as ke:
            print(ke)

    def find_contact(self, name):
        return self.contacts.__getitem__(name)

    def remove_contact(self, name):
        try:
            self.contacts.pop(name)
        except KeyError:
            return False
        else:
            return True

    def add_to_favorites(self, cont):
        if cont.name in self.contacts:
            self.favorites[cont.name] = cont.number

    def call(self, cont):
        print("Calling", cont.name)
        self.recent_calls[cont.name] = cont.number


# book = PhoneBook()

'''AM
There should be no ability to create instance of interface
Please create class and use it
class PhoneBookContact(IContact):
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    @property
    def name(self): return self.__name

    @property
    def number(self): return self.__number

    alexei = PhoneBookContact("Alexei", "06812345678")
'''
# alexei = IContact("Alexei", "06812345678")
# book.add_contact(alexei)
# anna = IContact("Anna", "05012345678")
# print(book.contacts)
# book.add_contact(alexei)
# print(book.contacts)
# print(book.find_contact("Alexei"))
# book.remove_contact("Rita")
# book.remove_contact("Alexei")
# print(book.contacts)
# book.add_contact(anna)
# print(book.contacts)
# book.add_to_favorites(anna)
# print(book.favorites)
# book.call(anna)
# print(book.recent_calls)
