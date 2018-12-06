
class A(object):
    
    attr2 = 'attr2'
    __attr3 = 'attr2'

    def __init__(self):
        self.attr1 = 'attr1'

    @staticmethod
    def my_method():
        print('A class')

class B(A):
    @staticmethod
    def my_method():
        A.my_method()

B.my_method()

A.attr2 = 'brocken'
a1 = A()
print(a1.__dict__)
print(A.__dict__)

a1._A__attr3

print(a1.attr1, a1.attr2)

