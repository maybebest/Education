import re

'''AM
Class name should represent functionality for which it was created
Contacts means that class represent functionality for several contacts
but in fact class represent one contact.
"Contact" is a good name in this case

Also here i meant that add_contact method could take any object which implements IContact interface
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

    @property    
    def name(self): return self.__name

    @property
    def phone(self): return self.__phone

...
def add_contact(self, contact: IContact):
    if self.validator.validate(contact.phone)
        self._constacts.append(contact)

PhoneBook(CustomValidator()).add_contact(PhoneBookContact())
'''
class Contacts(object):

    def __init__(self, name, number):
        self.name = name
        self.number = number


class Validator(object):

    @staticmethod
    def check_name(name):
        if name != '' and isinstance(name, str):
            return True

    @staticmethod
    def check_number(number):
        if number != '' and isinstance(number, str):
            if re.match(r'[8]{1}[0-9]{9}', number):
                return True
            else:
                print("Invalid number")





























