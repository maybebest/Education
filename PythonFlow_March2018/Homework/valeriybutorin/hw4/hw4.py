"""
# Homework 4 ##
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

My comments:
1. Contact just a object
2. Favorites - return Flag from contact - there is no specific logic to identify is_favorite
3. recent_calls - return all recent calls with  following formant contact full name and data-time
4. add_contact - validation for items count in list, if exist raise Exception
5. please uncomment some part of code for the checking.
"""
from Homework.valeriybutorin.hw4.entities.users import Vasil, Sveta, Igor
from Homework.valeriybutorin.hw4.validators.ReExpValidator import RegExpValidator
from Homework.valeriybutorin.hw4.entities.phone_book import PhoneBook
'''AM
"- add_contact should check contact's number with regex(or other)validator before add it to phone book
  (one validator per phone book instance)"
Requirement is not implemented
'''


SimplePhoneBook = PhoneBook(RegExpValidator)
SimplePhoneBook.add_contact(Vasil)
SimplePhoneBook.add_contact(Sveta)
# SimplePhoneBook.add_contact(Sveta) # - to check validation

SimplePhoneBook.call(Vasil)
SimplePhoneBook.call(Vasil)
SimplePhoneBook.call(Vasil)

SimplePhoneBook.call(Igor)

SimplePhoneBook.call(Sveta)
SimplePhoneBook.call(Sveta)

# SimplePhoneBook.recent_calls - to check property return all recent calls for contact
# SimplePhoneBook.favorites - to check property if the contact favorite

for c in SimplePhoneBook:
    print(c.__dict__)  # - return contact as a dict. It is required for checking ability to iterate by object.
