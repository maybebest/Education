"""__test_suite_runner_2.py"""

from geocoder.tests import LatLngTestCase
from fibonacci import FibonacciTestCase
import unittest

test_classes_to_run = [LatLngTestCase, FibonacciTestCase]

loader = unittest.TestLoader()

suites_list = []
for test_class in test_classes_to_run:
    suite = loader.loadTestsFromTestCase(test_class)
    print(suite) 
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)

runner = unittest.TextTestRunner()
results = runner.run(big_suite)
print(results)
