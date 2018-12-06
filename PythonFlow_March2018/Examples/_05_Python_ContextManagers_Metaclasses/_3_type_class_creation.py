"""Type. Class creation"""

class LatLng(object):
    """A class represention location coordinates"""

    def __init__(self, lat, lng):
        self.latitude = lat
        self.longitude = lng

############################

def __init__(self, lat, lng):
    self.latitude = lat
    self.longitude = lng

LatLng2 = type('LatLng2', (object,), {
               'latitude': None, 'longitude': None, '__init__': __init__})

print(LatLng2)  # <class '__main__.LatLng2'>
print(LatLng2(45, 45).latitude)  # 45
