## Homework 7 ##
# - All functionality from HW1(functions, classes, etc.) should be covered by tests.
#   Use built-in Python's Unittest framework
# - All functionality from HW4(functions, classes, etc.) should be covered by tests.
#   Use Pytest framework
# - All scenarios should be described in test cases (positive, negative, etc.)
# - Enjoy!

import pytest
from .hw4 import PhoneBook
from .hw4 import IContact

'''AM 
Please use setup_function for test data. 
def setup_function(function):
    #setup test data
test data (book, alexei,...) could be changed during the test but each test should have initial data
tests should be independent.

(not for rework - it is a good idea to have classes :))
'''

book = PhoneBook()
alexei = IContact("Alexei", "06812345678")
anna = IContact("Anna", "05012345678")
mal = IContact("Malformed", "string")


def test_add():
    book.add_contact(alexei)
    assert(book.contacts != None)


def test_find():
    assert(book.find_contact("Alexei"))


@pytest.mark.xfail
def test_find_negative():
    assert(book.find_contact("Alex") == None)


def test_removal():
    assert(book.remove_contact("Alexei") == True)


def test_removal_negative():
    assert(book.remove_contact("George") == False)


def test_favorites():
    book.add_to_favorites(anna)
    assert(book.favorites != None)


def test_call():
    book.call(anna)
    assert(book.recent_calls != None)

