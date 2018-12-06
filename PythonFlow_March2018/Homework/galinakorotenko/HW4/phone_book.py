from Homework.galinakorotenko.HW4.contacts import *
from collections import deque


'''AM
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

    @property    
    def name(self): return self.__name

    @property
    def phone(self): return self.__phone

...
def add_contact(self, contact: IContact):
    if self.validator.validate(contact.phone)
        self._constacts.append(contact)

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
class PhoneBook(object):
    def __init__(self, validator: IValidator):
        self.validator = validator;

PhoneBook(CustomValidator())
...
'''


class PhoneBook(Validator):
    """
    Class contains contact as object and methods for it
    """

    def __init__(self, name=None, number=None):
        self.name = name
        self.number = number
        self.contact_list = []
        self.favorite_list = []
        self.recent_calls = deque([], 10)

    def __iter__(self):
        return iter(self.contact_list)

    def add_contact(self, contact: Contacts):
        if Validator.check_name(contact.name) and Validator.check_number(contact.number):

            if contact not in self.contact_list:
                self.contact_list.append(contact)
                print("New contact was added", contact.__dict__)

            else:
                print("This contact exists in phone book")
        else:
            print("Invalid Contact data")

    def remove_contact(self, contact: Contacts):
        if contact in self.contact_list:
            self.contact_list.remove(contact)
            print("Contact {0} has been removed".format(contact.name))
        else:
            print("This contact {0} cannot be found at Contact list".format(contact.__dict__))

    def add_favorite(self, contact: Contacts):
        if contact in self.contact_list:
            self.favorite_list.append(contact)
            print("New Contact has been added to Your Favorites:", contact.__dict__)
        else:
            print("Please add this contact '{0}' to Contact list before".format(contact.name))

    def calling(self, contact: Contacts):
        if contact in self.contact_list:
            print("Calling to '{0}....".format(contact.name))
            self.recent_calls.append(contact)

    def find_contact(self, name):
        for contact in self.contact_list:
            if contact.name == name:
                print("Your contact details: {0} ".format(contact.__dict__))
            else:
                print("No contacts with this name")
        return contact

    @property
    def last_calls(self):
        return [i.__dict__.get('name') for i in self.recent_calls]

    @property
    def fav_list(self):
        return [i.__dict__.get('name') for i in self.favorite_list]

    @property
    def all_contacts(self):
        return [i.__dict__ for i in self.contact_list]


contact_1 = Contacts(name='Peter', number='8639876534')
contact_2 = Contacts(name='Mark', number='8634670534')
invalid_contact = Contacts(name='', number='2345678901')
contact_3 = Contacts(name='Steve', number='0987654456')

PB = PhoneBook()
PB.add_contact(contact_1)
PB.add_contact(contact_2)
PB.add_contact(invalid_contact)

print(PB.all_contacts)

PB.find_contact(name='Mark')
PB.find_contact(name='Steve')

PB.add_favorite(contact_2)
print(PB.fav_list)

PB.add_favorite(contact_3)

PB.calling(contact_1)
print(PB.last_calls)

PB.remove_contact(contact_3)
PB.remove_contact(contact_1)
print(PB.all_contacts)

it = iter(PB)
print(next(it))








