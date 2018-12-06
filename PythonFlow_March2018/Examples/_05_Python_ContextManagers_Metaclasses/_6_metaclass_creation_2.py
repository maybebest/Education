"""Type. New Metaclass"""

class MyMetaClass(type):
    def __call__(self):
        super(MyMetaClass, self).__call__()
        print('Call:', self.__class__)

class LatLng(object, metaclass=MyMetaClass):
    pass

class LatLng2(LatLng):   
    pass

A = LatLng()  # Call: <class '__main__.MyMetaClass'>
B = LatLng2() # Call: <class '__main__.MyMetaClass'>
