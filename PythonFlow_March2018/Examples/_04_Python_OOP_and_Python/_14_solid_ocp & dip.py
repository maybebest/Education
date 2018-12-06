"""SOLID. OCP & DIP"""

from _13_solid_srp_2 import IValidator, RegexEmailValidator, re

class CustomRegexEmailValidator(IValidator):
    def __init__(self, pattern):
        self.pattern = pattern

    def validate(self, email):
        return bool(re.search(self.pattern, email))

class Email(object):
    def __init__(self, email, validator: IValidator = RegexEmailValidator()):
        self.validator = validator
        if self.validator.validate(email):
            self.email = email
        else:
            print("Invalid email")

email1 = Email('example@example.com')
email2 = Email('example@example.com', CustomRegexEmailValidator('my_regex_pattern'))
# Invalid email

