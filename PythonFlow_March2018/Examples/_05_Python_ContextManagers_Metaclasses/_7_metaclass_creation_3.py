"""Type. Custom Metaclass"""

class ReadonlyAttrsMeta(type):
    def __setattr__(cls, attr, value):
        print('Trying set value "%s" to attribute "%s" of class "%s"' %
              (value, attr, cls.__name__))
        return  


class LatLng(object, metaclass=ReadonlyAttrsMeta):
    greenwich = (51.476852, -0.000500)


class LatLng2(LatLng):
    coords_precision = 6


del LatLng.greenwich 
# Trying set value "(0, 0)" to attribute "greenwich" of class "LatLng"

print(LatLng.greenwich)
# (51.476852, -0.0005)

LatLng2.coords_precision = (0, 0)
# Trying set value "(0, 0)" to attribute "coords_precision" of class "LatLng"

print(LatLng2.coords_precision)  # 6
