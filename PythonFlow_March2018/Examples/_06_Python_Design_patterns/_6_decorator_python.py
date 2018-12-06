"""Python Decorator example"""


def greenwich(cls):
    setattr(cls, 'greenwich', (51.4826, 0.0077))
    return cls


@greenwich
class LatLng(object):
    """A class represention location coordinates"""

    def __init__(self, lat, lng):
        self.latitude = lat
        self.longitude = lng

    def get_coords(self):
        return (self.latitude, self.longitude)


coords = LatLng(30, 45)
print(getattr(coords, 'greenwich'))
