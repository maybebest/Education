"""Homework 4
1- Implement PhoneBook class.
2- use OOP and SOLID
4- Class should contain methods:
- Enjoy! """

from abc import ABCMeta, abstractmethod
from collections import Iterable
import re
import validators


class IPhonebook(object):
    def __iter__(self):
        raise NotImplementedError("Method __iter__ is not implemented  for iterable")

"""3- Class should be an iterable (interface)."""
class Phonebook(Iterable):
    @abstractmethod
    def __init__(self):
        self.__contacts = []

    """5- add_contact method (take object: IContact and add it to phone book)."""
    def add_contact(self, contact):
        return self.__contacts.append(contact)

    """6- find_contact method (first match by name)"""
    """def __contains__(self, name):
        self.name in  """

    """7- remove_contact method (by name)"""
    try:
        def __delitem__(self, name):
            return self
    except NameError:
        print("Incorrect name")

    """8- add_to_favorites method (take object: IContact and add it to phone book (only if exists))"""
    def add_to_favorites(self, contact):
        return self.print('Calling to' + contact)

    """9- call method (take object: IContact and print 'Calling to <contact name>...'])"""

    """10- recent_calls property (returns recent calls<IContact>)"""
    @property
    def recent_calls(self):
        return self.__contacts

    """11- favorites property (returns favorites contacts<IContact>)"""
    @property
    def favorites_contacts(self):
        return self.__contacts

    """12- add_contact should check contact's number with regex(or other)validator before add it to phone book
  (one validator per phone book instance)"""

phonebook = Phonebook()
phonebook.add_contact('User1')
phonebook.add_contact('User2')

for contact in phonebook:
    print(contact)
