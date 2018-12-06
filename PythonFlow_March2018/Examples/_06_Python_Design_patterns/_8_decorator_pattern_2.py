"""Decorator Pattern example"""


def greenwich(decoratee):
    setattr(decoratee, 'greenwich', (51.4826, 0.0077))
    return decoratee


class LatLng(object):
    """A class represention location coordinates"""

    def __init__(self, lat, lng):
        self.latitude = lat
        self.longitude = lng


coords = LatLng(30, 45)

print(getattr(coords, 'greenwich', None))  # None

greenwich(coords)

print(getattr(coords, 'greenwich'))  # (51.4826, 0.0077)
