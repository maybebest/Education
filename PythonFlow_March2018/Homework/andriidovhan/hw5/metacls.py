
class MainCls(type):
    def __del__(cls):
        print('Destroying class {}'.format(cls.__name__))
    

class A(object, metaclass=MainCls):
    a='inside class A'
    
    def __del__(self):
        print('destroying instance of {} class'.format(self.__class__.__name__))

class B(A):
    b='inside class B'

a = A()
print(a.a)
b = B()
print(b.b)
