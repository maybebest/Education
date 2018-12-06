"""Latitude Longitude ou of range exception"""

from .lat_lng_exception import LatLngException

class LatLngOutOfRangeException(LatLngException):
    """Raised when the (lat, lng) is out of range"""

    def __init__(self, geopoint=(None, None)):
        super(LatLngOutOfRangeException, self).__init__(self.message)
        self.__lat, self.__lng = geopoint

    @property
    def message(self):
        return """Lat Lng is out of range. Valid coords: (-90 <= Lat <= 90) (-180 <= Lng <= 180)"""

    @property
    def geopoint(self):
        return (self.__lat, self.__lng)

