"""SOLID. SRP"""

import re, abc

class IValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self): pass

class RegexEmailValidator(IValidator):
    def validate(self, email):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

class Email(object):
    def __init__(self, email):
        self.validator = RegexEmailValidator()
        if self.validator.validate(email):
            self.email = email
        else:
            raise TypeError("Invalid email")

class Person(object):    
    def __init__(self, name, email):
        self.name, self.email_obj = name, Email(email)        

    def greet(self):
        print("Hi %s with email: %s! " % (self.name, self.email_obj.email))

# Person("Emelian", 'example@example.com').greet()
# Hi Emelian with email: example@example.com!