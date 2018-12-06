"""namedtuple(). Methods"""

from collections import namedtuple

LatLng = namedtuple('LatLng', 'lat lng')
COORDS = {11, 22}
# [11, 22] or (11, 22) or {'lat': 11, 'lng': 22} (for dict use COORDS = LatLng(**COORDS))

# makes a new instance from an existing sequence or iterable.
COORDS = LatLng._make(COORDS)
print(COORDS)  # LatLng(lat=11, lng=22)

# return a new instance of the named tuple replacing specified fields with new values
COORDS = COORDS._replace(lat=42)

# Tuple of strings listing the field names.
# Useful for introspection and for creating new named tuple types from existing named tuples.
print(COORDS._fields)  # ('lat', 'lng')

# returns a new OrderedDict
COORDS = COORDS._asdict()

print([COORDS['lat'], COORDS.get('lng')])  # [42, 22]
