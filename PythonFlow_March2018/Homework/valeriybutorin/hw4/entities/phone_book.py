from Homework.valeriybutorin.hw4.abstractions.abstarct_call import AbstractCall
from Homework.valeriybutorin.hw4.abstractions.abstarct_phone_book import AbstractPhoneBook
from Homework.valeriybutorin.hw4.entities.contact import Contact
from Homework.valeriybutorin.hw4.exeptions.phonebook_exeptions import ContactAlreadyExist
from Homework.valeriybutorin.hw4.iterfaces.iterable import Iterable

import datetime
import time


class PhoneBook(Iterable, AbstractCall, AbstractPhoneBook):
    def __init__(self, validator):
        self.__contacts = []
        self.__recent_calls = []
        self.validator = validator()

    def __iter__(self):
        return iter(self.__contacts)

    def call(self, contact: Contact):
        contact.recent_calls.append(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        return print("Calling to" + contact.full_name)

    def add_contact(self, contact: Contact):
        if self.validator.validate(contact):
            self.__contacts.append(contact)
        else:
            raise ContactAlreadyExist("Contact:  - Already in the Phone Book".format(contact.full_name))

    def remove_contact(self, contact: Contact):
        if self.__contacts.count(contact):
            self.__contacts.remove(contact)

    def find_contact(self, contact: Contact, full_name):
        return next(filter(lambda c: c.full_name == contact.full_name, self.__contacts))

    @property
    def recent_calls(self):
        return print(["Contact {0} - Recent calls: {1}".format(
            c.full_name, c.recent_calls) for c in self.__contacts if c.recent_calls])

    @property
    def favorites(self):
        return print(["Contact {0} - Favorite: {1}".format(
            c.full_name, c.favorite) for c in self.__contacts if c.recent_calls])