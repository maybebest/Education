"""OOP. User-Defined Exception Usage"""

from _7_custom_exceptions import LatLngOutOfRangeException


class LatLng(object):
    """A geopoint class"""

    def __init__(self, geopoint):
        self.geopoint = geopoint

    @property
    def geopoint(self):
        return (self.__lat, self.__lng)

    @geopoint.setter
    def geopoint(self, val):
        if self._is_valid(*val):
            self.__lat, self.__lng = val
        else:
            raise LatLngOutOfRangeException(val)

    def _is_valid(self, lat, lng):
        return -90 <= lat <= 90 and -180 <= lng <= 180


coords = LatLng((45, 45))
try:
    coords.geopoint = [200, 85]
except LatLngOutOfRangeException as ex:
    print(ex.message, ex.geopoint)
