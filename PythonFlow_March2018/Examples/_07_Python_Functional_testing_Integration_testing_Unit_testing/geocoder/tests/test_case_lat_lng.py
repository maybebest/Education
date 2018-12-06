"""Latitude Longitude Class Test"""

import unittest
from .. import LatLng
from ..exceptions import LatLngOutOfRangeException

class LatLngTestCase(unittest.TestCase):
    """Tests for `LatLng`."""

    def setUp(self):
        """test fixture. called before each test method in test case"""
        self.lat_lng = LatLng((20, 50))

    def test_geopoint_has_value(self):
        self.assertTrue(self.lat_lng.geopoint)

    def test_invalid_geopoint_value(self):
        with self.assertRaises(LatLngOutOfRangeException):
            self.lat_lng.geopoint = (200, 100)

    def tearDown(self):
        del self.lat_lng

# class LatLngTestCase(unittest.TestCase):
#     """Tests for `LatLng`."""

#     @classmethod
#     def setUpClass(cls):
#         """test fixture. called before each test case"""
#         cls.lat_lng = LatLng((20, 50))

#     def test_geopoint_has_value(self):
#         self.assertTrue(self.lat_lng.geopoint)

#     def test_invalid_geopoint_value(self):
#         with self.assertRaises(LatLngOutOfRangeException):
#             self.lat_lng.geopoint = (200, 100)

#     @classmethod
#     def tearDownClass(cls):
#         del cls.lat_lng
