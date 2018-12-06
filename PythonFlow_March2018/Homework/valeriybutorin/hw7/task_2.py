"""
- All functionality from HW4(functions, classes, etc.) should be covered by tests.
  Use Pytest framework
- All scenarios should be described in test cases (positive, negative, etc.)
"""
import pytest

from Homework.valeriybutorin.hw4.entities.contact import Contact
from Homework.valeriybutorin.hw4.entities.phone_book import PhoneBook
from Homework.valeriybutorin.hw4.entities.users import Vasil, Sveta
from Homework.valeriybutorin.hw4.exeptions.phonebook_exeptions import ContactAlreadyExist
from Homework.valeriybutorin.hw4.validators.ReExpValidator import RegExpValidator


class TestHomeWork4PhoneBook(object):
    @pytest.fixture(scope="function")
    def phone_book(self):
        return PhoneBook(RegExpValidator)

    def test_positive_add_contact(self, phone_book):
        """Check that contact added without exceptions"""
        assert phone_book.add_contact(Vasil) is None, "add contact executed without errors"

    def test_impossible_add_identical_contact(self, phone_book):
        """Check that impossible to add two identical contacts"""
        with pytest.raises(ContactAlreadyExist) as e:
            phone_book.add_contact(Sveta)
            phone_book.add_contact(Sveta)

    def test_positive_call_to_user(self, phone_book):
        """Check that possible call to added user without exceptions"""
        phone_book.add_contact(Vasil)
        assert phone_book.call(Vasil) is None, "call executed without errors"

    def test_positive_recent_call_is_empty(self, phone_book):
        """Check that possible call to added user without exceptions"""
        phone_book.add_contact(Vasil)
        assert phone_book.remove_contact(Vasil) is None, "remove_contact executed without errors"
        assert phone_book.recent_calls is None, "contact should be removed from recent calls"

    def test_positive_remove_contact(self, phone_book):
        """Check that possible remove contact user without exceptions"""
        phone_book.add_contact(Vasil)
        assert phone_book.remove_contact(Vasil) is None, "remove_contact executed without errors"
        assert phone_book.recent_calls is None, "contact should be removed from recent calls"

    def test_negative_remove_contact(self, phone_book):
        """Check that possible remove  one contact twice"""
        phone_book.add_contact(Vasil)
        assert phone_book.remove_contact(Vasil) is None, "remove_contact executed without errors"
        assert phone_book.recent_calls is None, "contact should be removed from recent calls"
        assert phone_book.remove_contact(Vasil) is "Contact in not in list", "validation message should be returned"

    def test_negative_get_favorite(self, phone_book):
        """Check that possible favorites always empty"""
        assert phone_book.favorites is None, "Favorites Should be empty"

    def test_positive_get_favorite(self, phone_book):
        """Check that possible favorites are available"""
        phone_book.add_contact(Vasil)
        phone_book.call(Vasil)

        assert Vasil in phone_book.favorites, "After call contact should be in favorites"


class TestHomeWork4Contact(object):
    @pytest.fixture(scope="function")
    def contact(self):
        return Contact(first_name="Vlad",
                       last_name="Pavlov",
                       age=30,
                       phone_number="423-423-4234",
                       gender="Male")

    def test_valid_contact(self, contact):
        """Check that possible map contact to dict"""
        expected_dict = {'age': 30,
                         'gender': 'Male',
                         'first_name': 'Vlad',
                         'last_name': 'Pavlov',
                         'phone_number': '423-423-4234',
                         'recent_calls': [],
                         'favorite': False}
        assert contact.__dict__ == expected_dict, "Object Contact should be equel to expected dict"

    def test_valid_empty_contact(self):
        """Check that possible create contact with all empty attr"""
        empty_contact_object = Contact(first_name=None,
                                       last_name=None,
                                       age=None,
                                       phone_number=None,
                                       gender=None)
        empty_contact_dict = dict(first_name=None,
                                  last_name=None,
                                  age=None,
                                  phone_number=None,
                                  gender=None)
        assert empty_contact_object.__dict__ == empty_contact_dict, \
            "It is impossible to create Contact with empty attributes"
