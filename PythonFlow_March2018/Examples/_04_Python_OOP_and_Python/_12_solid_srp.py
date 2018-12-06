"""SOLID. SRP"""

import re
class Person(object):
    """Person class"""
    name = None
    email = None

    def __init__(self, name, email):
        self.name = name
        if self.validateEmail(email):
            self.email = email
        else:
            raise TypeError("Invalid email")

    def validateEmail(self, email):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

    def greet(self):
        print("Hi %s!" % self.name)

print(Person("Emelian", 'example@example.com').name)  # Emelian