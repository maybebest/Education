"""
- Implement Singleton metaclass
  which may be used as metaclass for other classes making their instances Singletons
"""


class MetaSingleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class TestMetaSingleton(object, metaclass=MetaSingleton):
    pass


test1 = TestMetaSingleton()
test2 = TestMetaSingleton()

assert test1 == test2, "Class must have the same link in the memory"
