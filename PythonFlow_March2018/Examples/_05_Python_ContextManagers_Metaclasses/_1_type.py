"""Type"""

class LatLng(object):
    """A class represention location coordinates"""

    def __init__(self, lat, lng):
        self.latitude = lat
        self.longitude = lng

print(type(LatLng))  # <class 'type'>

coord = LatLng(45, 45)
print(type(coord))  # <class '__main__.LatLng'>

print(isinstance(coord, LatLng), isinstance(LatLng, type))  # True True