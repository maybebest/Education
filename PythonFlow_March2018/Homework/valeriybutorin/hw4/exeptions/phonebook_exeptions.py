'''AM (not for rework)
It is a good idea to have base exception class for you package f.e.

class PhoneBookException(Exception):
    pass

class ContactAlreadyExist(PhoneBookException):
    pass

class ContactInvalidPhoneNumber(PhoneBookException):
    pass

............

This is a good idea because all phone number exception could be handled in one except:

try:
    #do something with phone book
except PhoneBookException:
    # here could be any exception which derived from PhoneBookException

'''
class ContactAlreadyExist(Exception):
    pass