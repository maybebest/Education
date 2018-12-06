
class M(type):
    def __new__(cls, class_name, bases, attr):
        def __del__(self):
            print('Del instance')

        attr['__del__'] = __del__

        return super().__new__(cls, class_name, bases, attr)
    def __del__(cls):
        print('Dell class')


class A(object, metaclass=M):
    pass    

class B(A):
    pass
B()


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

print(Singleton() is Singleton())


class CM(object):
    def __enter__(self):
        print('enter')

    def __exit__(self, arg1, arg2, arg3):
        return True
with CM():
    raise ValueError()