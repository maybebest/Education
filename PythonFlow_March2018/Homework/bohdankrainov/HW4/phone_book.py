from Homework.bohdankrainov.HW4.contacts import IContact, PhoneBookContact
from Homework.bohdankrainov.HW4.validator import Validator, IValidator

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


class PhoneBook(object):

    def __init__(self, validator: IValidator):
        self.validator = validator
        self._contacts = []
        self.calls = []

    def __iter__(self):
        return iter(self._contacts)

    def add_contact(self, contact: IContact):
        if self.validator.validate(contact):
            contact.__setattr__('favorite', False)
            print('Adding {0} contact to Phone Book'.format(contact.__dict__))
            return self._contacts.append(contact)
        else:
            print('Phone incorrect!', contact.phone)
            return False

    def find_contact(self, name: str):
        try:
            return [i for i in self._contacts if i.name == name][0]
        except IndexError:
            print("Contact name '{}' was not found".format(name))
            return False

    def remove_contact(self, name: str):
        cont = self.find_contact(name)
        if isinstance(cont, IContact):
            print("Contact {0} will be removed".format(cont.__dict__))
            self._contacts.remove(cont)
            return True
        elif cont is False:
            return cont

    def calling(self, contact_name: str):
        cont = self.find_contact(contact_name)
        if isinstance(cont, IContact):
            self.calls.append(cont)
            return "Calling to {0}\n{1}".format(cont.name, cont.phone)

    def add_to_favorites(self, name: str):
        cont = self.find_contact(name)
        if isinstance(cont, IContact):
            cont.favorite = True
            print("Contact name '{0}' added to favorites".format(name))
            return cont.__dict__

    @property
    def favorites(self):
        return [f.__dict__ for f in self._contacts if f.favorite]

    @property
    def recent_calls(self):
        return [call.__dict__ for call in self.calls]


valid = Validator("^[0-9]{6,13}$")
contact1 = PhoneBookContact('John', '0633215879')
contact2 = PhoneBookContact('John', '0736981596')
contact3 = PhoneBookContact('Bill', '0991237854')
contact4 = PhoneBookContact('Ann', '0982571986')
contact5 = PhoneBookContact('Andy', '0501987364')
incor_contact = PhoneBookContact('Test', 'text')
PB = PhoneBook(valid)

PB.add_contact(contact1)
PB.add_contact(contact2)
PB.add_contact(contact3)
PB.add_contact(contact4)
PB.add_contact(contact5)
PB.add_contact(incor_contact)

for i in ['Bill', 'John', 'Test', 'Ann', 'Jack']:
    find = PB.find_contact(i)
    if find:
        print('Search result:', find.__dict__)
    else:
        print(find)

print(PB.calling('Andy'))
print(PB.remove_contact('John'))
print(PB.remove_contact('Ann'))

PB.add_contact(contact1)
PB.add_to_favorites('Bill')
PB.add_to_favorites('Bob')
PB.add_to_favorites('Andy')

print('Favorite contacts:', PB.favorites)
print('Recent calls:', PB.recent_calls)

it = iter(PB)

for el in range(len(PB._contacts)):
    c = next(it)
    print(c, c.__dict__)

