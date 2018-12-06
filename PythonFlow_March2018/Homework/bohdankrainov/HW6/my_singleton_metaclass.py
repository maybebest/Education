class SignMetaClass(type):

    def __call__(cls, *args, **kwargs):
        if getattr(cls, 'instance', None) is None:
            cls.instance = super(cls, cls).__new__(cls, *args, **kwargs)
        return cls.instance


class AAA(object, metaclass=SignMetaClass):
    pass


a = AAA()
print('First instance:', a.instance)
b = AAA()
print('Second instance:', b.instance)
print(a, b)
print(a is b)
print(AAA() is AAA())
print(id(a), id(b))
