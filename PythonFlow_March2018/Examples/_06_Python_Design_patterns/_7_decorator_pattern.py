"""Decorator Pattern example"""


class Greenwich(object):
    greenwich = (51.4826, 0.0077)

    def __new__(self, decoratee):
        setattr(decoratee, 'greenwich', self.greenwich)
        return decoratee


class LatLng(object):
    """A class represention location coordinates"""

    def __init__(self, lat, lng):
        self.latitude = lat
        self.longitude = lng


coords = LatLng(30, 45)

decorated_coords = Greenwich(coords)

print(type(decorated_coords))  # <class '__main__.LatLng'>
print(isinstance(decorated_coords, LatLng))  # True

print(decorated_coords.greenwich)  # (51.4826, 0.0077)
