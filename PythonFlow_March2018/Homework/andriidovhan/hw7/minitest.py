import unittest
# from Homework.andriidovhan.hw1.my_filter import my_filter
import Homework.andriidovhan.hw1
# from Homework.andriidovhan.hw1.my_map import my_map
# from Homework.andriidovhan.hw1.my_uniq import my_uniq
# import ..hw1

class TestHW1(unittest.TestCase):

    def test_my_find(self):
        self.assertEqual(my_find("test"), "test", " fn should return sstring")
