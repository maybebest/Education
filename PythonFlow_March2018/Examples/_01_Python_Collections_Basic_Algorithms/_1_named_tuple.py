"""namedtuple()"""

from collections import namedtuple

LatLng = namedtuple('LatLng', ['lat', 'lng'])
# LatLng = namedtuple('LatLng', 'lat, lng')
# LatLng = namedtuple('LatLng', 'lat lng')

COORDS = [LatLng(45, lng=68), LatLng(58, 32)]

print(COORDS)
# [LatLng(lat=45, lng=68), LatLng(lat=58, lng=32)]

print(type(COORDS[0]))
# <class '__main__.LatLng'>

for coord in COORDS:
    print('lat: %d, lng: %d' % (coord.lat, coord[1]))
# lat: 45, lng: 68
# lat: 58, lng: 32
