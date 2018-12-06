class MainCls(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(MainCls, cls).__call__(*args, **kwargs)
        return cls.__instance
    

class A(object, metaclass=MainCls):
    a='attr 1'
    b='attr 2'

a = A()
print(id(a))

b = A()
print(id(a))