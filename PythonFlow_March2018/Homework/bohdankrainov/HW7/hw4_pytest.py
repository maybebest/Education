import pytest
from Homework.bohdankrainov.HW4 import contacts, phone_book, validator


class TestPhoneBook:

    '''AM
    Please use 'setup_method' for test data (PBook, created_contacts) - setup test data for each test
    Tests should be independent from each other, 
    but in your case test data could be changed during the tests 
    and other tests will be affected
    '''
    @classmethod
    def setup_class(cls):
        cls.created_contacts = []

    def setup_method(self):
        self.test_validator = validator.Validator("^[0-9]{6,13}$")
        self.PBook = phone_book.PhoneBook(self.test_validator)

    def test_contact_adding_to_phone_book_positive(self):
        test_cont1 = contacts.PhoneBookContact('TestContact1', '0503185714')
        self.created_contacts.append(test_cont1)
        print('\nNew test contact:', self.created_contacts[-1].__dict__)
        assert self.PBook.add_contact(test_cont1) is not False and test_cont1 in self.PBook._contacts, \
            "{0} contact is not added to Phone Book".format(test_cont1.__dict__)

    def test_contact_adding_to_phone_book_negative(self):
        incorrect_cont = contacts.PhoneBookContact('TestContact2', '531131343231346544')
        assert self.PBook.add_contact(incorrect_cont) is False, \
            '{0} incorrect contact successfully added to Phone Book'.format(incorrect_cont.__dict__)

    def test_call_to_contact_positive(self):
        test_cont2 = contacts.PhoneBookContact('TestCallContact', '0685284688')
        self.PBook.add_contact(test_cont2)
        assert test_cont2 in self.PBook._contacts, 'Contact adding to Phone Book failed'
        test_call = self.PBook.calling(test_cont2.name)
        assert test_call is not None and test_cont2 in self.PBook.calls, 'Calling is failed'
        print('Result of the test call:', test_call)

    def test_call_to_contact_negative(self):
        test_call = self.PBook.calling('Incorrect')
        print('Result of the test call:', test_call)
        assert test_call is None, 'Calling to incorrect contact was successful'

    def test_add_to_favorite_positive(self):
        test_cont3 = contacts.PhoneBookContact('TestFavoriteContact', '0916141388')
        self.created_contacts.append(test_cont3)
        self.PBook.add_contact(test_cont3)
        assert test_cont3 == self.PBook._contacts[-1], 'Contact was not added'
        assert self.PBook._contacts[-1].__dict__.get('favorite') is False, 'Contact added to favorite with out request'
        self.PBook.add_to_favorites('TestFavoriteContact')
        print(self.PBook.favorites)
        assert self.PBook._contacts[-1].__dict__.get('favorite') is True, 'Contact was not added to favorite'

    def test_add_to_favorite_negative(self):
        assert self.PBook.add_to_favorites('Incorrect') is None, 'Non existed contact added to favorite'

    def test_recent_calls_property(self):
        test_cont4 = contacts.PhoneBookContact('TestRecentCallsContact', '0735941684')
        self.created_contacts.append(test_cont4)
        self.PBook.add_contact(test_cont4)
        print(self.PBook.calling('TestRecentCallsContact'))
        assert test_cont4.__dict__ in self.PBook.recent_calls

    def test_remove_contact_positive(self):
        test_cont5 = contacts.PhoneBookContact('TestRemoveContact', '0991548965')
        self.created_contacts.append(test_cont5)
        self.PBook.add_contact(test_cont5)
        assert test_cont5 in self.PBook._contacts, 'Contact adding to Phone Book failed'
        self.PBook.remove_contact('TestRemoveContact')
        assert self.PBook.find_contact('TestRemoveContact') is False and test_cont5 not in self.PBook._contacts, \
            'Contact removing failed'

    def test_remove_contact_negative(self):
        assert self.PBook.remove_contact('IncorrectName') is False, 'Non existed contact removing passed'

    def teardown_method(self):
        print('\nCreated Phone Book instance for this test:\n{0}-->{1}\n'.format(self.PBook, self.PBook.__dict__))

    def teardown_class(self):
        print('\n\nCreated contacts during test suite execution:\n', [(cont.name, cont.phone)
                                                                      for cont in self.created_contacts])


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s', '--color=yes'])
