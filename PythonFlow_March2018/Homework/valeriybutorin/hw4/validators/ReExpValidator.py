import re

from Homework.valeriybutorin.hw4.entities.contact import Contact
from Homework.valeriybutorin.hw4.iterfaces.validable import Validable


class RegExpValidator(Validable):

    def validate(self, contact: Contact):
        return re.match("^[1-9][0-9]{10,14}$", contact.phone_number)