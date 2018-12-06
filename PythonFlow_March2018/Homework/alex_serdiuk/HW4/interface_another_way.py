"""- Implement PhoneBook class.
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
  (one validator per phone book instance)"""

from abc import ABCMeta, abstractmethod

#Interface
class PhoneBook(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def add_contact(self, name): pass

    @abstractmethod
    def find_contact(self): pass

    @abstractmethod
    def remove_contact(self): pass

    @abstractmethod
    def add_to_favorites(self): pass

    @abstractmethod
    def call(self): pass

    @property
    def recent_calls(self): pass

    @property
    def favorites(self): pass

class Contacts(PhoneBook):

    def __init__(self):
        self.phone_book = []
        self.favorites = []

        super(Contacts, self).__init__()

    def add_contact(self, name):
        return self.phone_book.append(name)


contact1 = Contacts("Ivan ", 234589, "today")

print(contact1.add_contact("ivan"))




