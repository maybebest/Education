"""Type. Custom Metaclass"""

class InstancesReadonlyAttrsMeta(type):
    def __new__(cls, name, bases, dct):
        def __setattr__(self, attr, value):
            print('Trying set value "%s" to instance attribute "%s" (class "%s")' %
                  (value, attr, self.__class__.__name__))
            return

        attrs = dict(dct)
        attrs['__setattr__'] = __setattr__
        return super(InstancesReadonlyAttrsMeta, cls).__new__(cls, name, bases, attrs)

class LatLng(object, metaclass=InstancesReadonlyAttrsMeta):
    greenwich = (51.476852, -0.000500)


lat_lng = LatLng()
print(lat_lng.greenwich)  # (51.476852, -0.0005)

lat_lng.greenwich = (0, 0)
# Trying set value "(0, 0)" to instance attribute "greenwich" (class "LatLng")

print(lat_lng.greenwich)  # (51.476852, -0.0005)
