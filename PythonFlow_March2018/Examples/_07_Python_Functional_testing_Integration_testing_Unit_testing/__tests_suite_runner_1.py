"""__test_suite_runner.py"""

import geocoder.tests
import fibonacci
import unittest


def suite():
    suite = unittest.TestSuite()
    # test method name should be defined here (in this case)
    suite.addTest(geocoder.tests.LatLngTestCase('test_geopoint_has_value'))
    suite.addTest(fibonacci.FibonacciTestCase(
        'test_fibonacci_number_25_less_than_limit'))
    return suite


runner = unittest.TextTestRunner()
runner.run(suite())
