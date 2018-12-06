"""OOP. User-Defined Exception"""


class LatLngException(Exception):
    """Base class for other LatLng Exceptions"""
    pass


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
