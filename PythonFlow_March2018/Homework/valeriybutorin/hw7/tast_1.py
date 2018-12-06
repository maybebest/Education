"""
- All functionality from HW1(functions, classes, etc.) should be covered by tests.
  Use built-in Python's Unittest framework
"""
import unittest
from Homework.valeriybutorin.test_data.test_data import tuple_to_test, list_to_test

from Homework.valeriybutorin.hw1.hw_1 import find_str_one, get_unique_collection, filter_by_type, map_items_to_str, \
    find_first_element_by_type
from Homework.valeriybutorin.utils.utils import is_int, map_to_string


'''AM
I think it is a good idea to have initial (new) test data for each test 
because independent tests is a bad practice.
For example:
from Homework.valeriybutorin.test_data.test_data import tuple_to_test, list_to_test
...
list_to_test could be changed during test execution and 
next test will have modified data which in my opinion is a bad practice.

As a solution list_to_test could be a function which each time returns new list
def list_to_test():
    return [1, 2, 3, 4, 5, 6, 6, False, "one_two", "one", False, "one_three", "ponep"]

...
actual_result = (map_items_to_str(list_to_test(), map_to_string))
...

in this case you a guarantee initial test data for each test

also setup fixtures could be used here
'''
class TestHomeWork1(unittest.TestCase):

    def test_positive_find_str_one(self):
        """Check if fn return one for value one in lowercase"""
        self.assertEqual(find_str_one("one"), "one", " fn should return string one")

    def test_negative_find_str_one_with_uppercase(self):
        """Check if fn return one for value one in uppercase"""
        self.assertEqual(find_str_one("ONE"), "one", "fn should return string one")

    def test_negative_find_str_one_with_camelcase(self):
        """Check if fn return one for value one in camelcase"""
        self.assertEqual(find_str_one("oNe"), "one", "fn should return string one")

    def test_positive_find_str_one_return_none(self):
        """Check if fn return None for any value except one"""
        self.assertEqual(find_str_one("zzz"), None, "fn should return None if value not string one")

    def test_positive_get_unique_collection_for_list(self):
        """Check if fn return unique values with type list"""
        actual_result = get_unique_collection(list_to_test)
        expected_result = [1, 2, 3, 4, 5, 6, False, 'one_two', 'one', 'one_three', 'ponep']
        self.assertEqual(actual_result, expected_result, "fn should returns only unique values")
        self.assertEqual(type(actual_result), list, "fn should return type list")

    def test_positive_get_unique_collection_for_tuple(self):
        """Check if fn return unique values with type tuple"""
        actual_result = get_unique_collection(tuple_to_test)
        expected_result = (1, 2, 3, 4, "ponep", "one")
        self.assertEqual(actual_result, expected_result, "fn should returns only unique values")
        self.assertEqual(type(actual_result), tuple, "fn should return type tuple")

    def test_negative_get_unique_collection_for_dict(self):
        """Check if fn return ValueError if data type is dict"""
        with self.assertRaises(ValueError) as context:
            get_unique_collection({"key": "value"})

        self.assertTrue(context.exception, "ValueError should be raised")

    def test_positive_filter_by_type_only_ints(self):
        """Check if fn return only ints"""
        self.assertEqual(filter_by_type(is_int, list_to_test), [1, 2, 3, 4, 5, 6, 6], "fn should return only ints")

    def test_positive_filter_by_type_only_strs(self):
        """Check if fn return only strs"""
        self.assertEqual(filter_by_type(lambda x: type(x) == str, list_to_test),
                         ['one_two', 'one', 'one_three', 'ponep'], "fn should return only strs")

    def test_negative_filter_by_type_only_lists(self):
        """Check if fn return only lists"""
        self.assertEqual(filter_by_type(lambda x: type(x) == list, list_to_test),
                         [], "fn should return only lists")

    def test_positive_map_items_to_str_with_list(self):
        """Check that fn return only str"""
        actual_result = (map_items_to_str(list_to_test, map_to_string))
        expected_result = ['1', '2', '3', '4', '5', '6', '6', 'False', 'one_two', 'one', 'False', 'one_three', 'ponep']
        self.assertEqual(actual_result, expected_result, "All elements in sequence should be str")

    def test_positive_map_items_to_str_with_classes(self):
        """Check that fn return only str"""
        test_data = [ChildProcessError]
        actual_result = (map_items_to_str(test_data, map_to_string))
        expected_result = ["<class 'ChildProcessError'>"]
        self.assertEqual(actual_result, expected_result, "All elements in sequence should be str")

    def test_positive_map_items_to_str_with_booleans(self):
        """Check that fn return only str"""
        test_data = [True, False]
        actual_result = (map_items_to_str(test_data, map_to_string))
        expected_result = ['True', 'False']
        self.assertEqual(actual_result, expected_result, "All elements in sequence should be str")

    def test_positive_find_first_element_by_type(self):
        """Check that fn returns string with value one"""
        self.assertEqual(find_first_element_by_type(find_str_one, list_to_test), "one", "fn should return  string one")

    def test_negative_find_first_element_by_type_with_true(self):
        """Check that fn returns boolena True"""
        self.assertEqual(find_first_element_by_type(lambda x: x is True, list_to_test), "True", "fn should return True")


if __name__ == '__main__':
    unittest.main()
