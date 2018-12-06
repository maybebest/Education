import re
import abc


class Iterable(object):
    def __iter__(self):
        '''AM
        "raise" should raise instance of error not error type.
        Please use following construction:
        raise NotImplementedError('__iter__ is not implemented')
        '''
        raise NotImplementedError('__iter__ is not implemented')


'''AM
I think this interface could be used(and used now) for PhoneBook class to 
say that PhoneBook class should have add_contact, find_contact, remove_contact method
This means that this interface could you any class which wants to be a phone book.
I'm trying to say that current name IContact is not suit for this interface
I think this interface should have name IContactBook
'''


class IContactBook(object):
    def add_contact(self, new_contact={}):
        raise NotImplementedError

    def find_contact(self):
        raise NotImplementedError

    def remove_contact(self):
        raise NotImplementedError


class IContac(abc.ABC):
    pass

    @property
    @abc.abstractmethod
    def phone_number(self): pass

'''AM (not for rework)
Looks like this is extra class
[pylint] E0102:class already defined line 46
It could be deleted
'''
class Contact(IContac):
    def __init__(self, new_contact={}):
        # import pdb; pdb.set_trace()
        contact = new_contact
        contact.update({'favorite': False})
        self.contact = contact

    @property
    @abc.abstractmethod
    def name(self): pass

    @property
    @abc.abstractmethod
    def phone_number(self): pass


class Contact(IContac):
    '''AM (not for rework)
    Extra dictionary usage here. It could be written easier
    def __init__(self, name, number):
        self.__name, self.__phone_number = name, number
        self.favorite = false
    @property
    def name(self):
        return self.__name
    ....
    pb.add_contact(Contact('Igor', '123'}))
    '''
    def __init__(self, new_contact={}):
        # import pdb; pdb.set_trace()
        contact = new_contact
        contact.update({'favorite': False})
        self.contact = contact

    @property
    def name(self):
        return self.contact['name']

    @property
    def phone_number(self):
        return self.contact['phone_number']

    @property
    def favorite(self):
        return self.contact['favorite']


class IValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self): pass


class RegexPhoneNumberValidator(IValidator):
    def validate(self, phone_number):
        return bool(re.search(r"^[0-9]+$", phone_number))


class PhoneBook(Iterable, IContactBook):
    def __init__(self, validator: IValidator = RegexPhoneNumberValidator()):
        self.validator = validator
        self.contacts = []
        self.recent_cals = []

    def __iter__(self):
        return iter(self.contacts)

    '''AM (not for rework)
    Here i meant following signature
    def add_contact(self, new_contact: IContact):
        #...
        # self.contacts.append(new_contact)
    Such signature say that this function could take any object which implements IContact interface
    Not only just Contact type    
    '''
    def add_contact(self, new_contact: Contact):
        if self.validator.validate(new_contact.phone_number):
            self.contacts.append(new_contact.contact)

    def find_contact(self, pattern):
        for c in self.contacts:
            if c['phone_number'] == pattern or c['name'] == str(pattern):
                yield c

    def remove_contact(self, pattern):
        for c in self.contacts:
            if c['phone_number'] == pattern or c['name'] == str(pattern):
                self.contacts.remove(c)

    def add_to_favorites(self, pattern):
        for c in self.contacts:
            if c['phone_number'] == pattern or c['name'] == str(pattern):
                c['favorite'] = True

    def show_favorites(self):
        for c in self.contacts:
            if c['favorite']:
                print(c)

    def call(self, pattern):
        for c in self.contacts:
            if c['phone_number'] == str(pattern) or c['name'] == pattern:
                print('Callint to {}:{}'.format(c['name'], c['phone_number']))
                self.recent_cals.append(c)
                break

    @property
    def recent_calls(self):
        print(self.recent_cals)


pb = PhoneBook(RegexPhoneNumberValidator())
print('add_contact')
pb.add_contact(Contact(new_contact={'name': 'Igor', 'phone_number': '123'}))
pb.add_contact(Contact(new_contact={'name': 'Igor', 'phone_number': '123'}))
pb.add_contact(Contact(new_contact={'name': 'Oleh', 'phone_number': '345'}))
pb.add_contact(Contact(new_contact={'name': 'Masha', 'phone_number': '456'}))
pb.add_contact(Contact(new_contact={'name': 'Vika', 'phone_number': '567'}))
print('find_contact')
print(next(pb.find_contact('Igor')))
print('remove_contact')
pb.remove_contact('Oleh')

print('add_to_favorites')
pb.add_to_favorites('456')
pb.add_to_favorites('567')
print('show_favorites')
pb.show_favorites()
print('call')
pb.call(456)
print('recent_calls')
pb.recent_calls

print('all contacts')
for c in pb.contacts:
    print(c)
# class PhoneBook(Iterable, IContact):
#     def __init__(self):
#         self.__contacts = []
#         self.__recent_cals = []

#     def __iter__(self):
#         return iter(self.__contacts)

#     '''AM
#     "add_contact method (take object: IContact and add it to phone book)"
#     Here i meant that should be one more interface - IContact
#     class IContact(ABC):
#         @property
#         @abstractmethod
#         def name: pass

#         @property
#         @abstractmethod
#         def number: pass

#     class Contact(IContact):
#         def __init__(self, name, number):
#             self.__name, self.__number = name, number

#         @property
#         def name: return self.__name

#         @property
#         def number: return self.__number

#     pb = PhoneBook(RegexValidator())
#     pb.add_contact(Contact('Andrew', '123456'))
#     ..........
#     def add_contact(self, new_contact: IContact):
#         #do something
#     '''
#     def add_contact(self, new_contact={}):
#         # import pdb; pdb.set_trace()
#         if bool(new_contact):
#             '''AM
#             Please move validation logic to new class RegexEmailValidator
#             1) this class should implement IValidator interface (interface has abstract validate method)
#             2) instance of this class should be passed to PhoneBook constructor

#             class PhoneBook(Iterable, IPhoneBook):
#                 def __init__(self, validator: IValidator = RegexEmailValidator()):
#                     self.__validator = validator
#             ....
#             def add_contact(self, new_contact: IContact):
#                 if self.__validator.validate(new_contact.number):
#                     add
#             ...
#             pb = PhoneBook(RegexValidator())

#             '''
#             if re.match("^[0-9]+$", str(new_contact['phone_number'])):
#                 contact = new_contact
#                 contact.update({'favorite':False})
#                 self.__contacts.append(contact)
#             else:
#                 print('Phone number should be sequence of digits')
#         else:
#             print('please, pass new contact parameter as new_contact=\{name\: "<name>", phone_number: "<number>"}')

#     def find_contact(self, pattern):
#         for contact in self.__contacts:
#             if contact['phone_number']==pattern or contact['name']==pattern:
#                 yield contact

#     def remove_contact(self, pattern):
#         for contact in self.__contacts:
#             if contact['phone_number']==pattern or contact['name']==pattern:
#                 self.__contacts.remove(contact)

#     def add_to_favorites(self, pattern):
#         for contact in self.__contacts:
#             if contact['phone_number']==pattern or contact['name']==pattern:
#                 contact['favorite']=True

#     def show_favorites(self):
#         for contact in self.__contacts:
#             if contact['favorite']:
#                 print(contact)

#     def call(self, pattern):
#         for contact in self.__contacts:
#             if contact['phone_number']==pattern or contact['name']==pattern:
#                 print('Callint to {}:{}'.format(contact['name'], contact['phone_number']))
#                 self.__recent_cals.append(contact)
#                 break

#     @property
#     def recent_calls(self):
#         print(self.__recent_cals)

# contact_book = PhoneBook()
# print('add_contact')
# contact_book.add_contact(new_contact={'name':'Ivan', 'phone_number':123})
# contact_book.add_contact(new_contact={'name':'Vova', 'phone_number':456})
# contact_book.add_contact(new_contact={'name':'Igor', 'phone_number':789})
# contact_book.add_contact(new_contact={'name':'Igor', 'phone_number':789})
# contact_book.add_contact(new_contact={'name':'Oleh', 'phone_number':111})
# print('find_contact')
# contact_book.find_contact('Igor')
# print(next(contact_book.find_contact(111)))
# print('remove_contact')
# contact_book.remove_contact(123)
# print('add_to_faforites')
# contact_book.add_to_favorites(111)
# contact_book.add_to_favorites(789)
# print('show_favorites')
# contact_book.show_favorites()
# print('call')
# contact_book.call(789)
# contact_book.call(456)
# print('recent_calls')
# contact_book.recent_calls
