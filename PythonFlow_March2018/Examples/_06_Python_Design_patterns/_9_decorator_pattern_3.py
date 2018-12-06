"""Decorator Pattern example"""


class Engine(object):
    pass


class Car(object):
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        print('Driving')


class Tuning(object):
    color = None

    def __new__(self, decoratee, color):
        self.color = color
        setattr(decoratee, 'color', self.color)
        return decoratee


my_car = Car()
tuned_car = Tuning(my_car, color='red')
print(tuned_car.__dict__)
# {'color': 'red', 'engine': <__main__.Engine object at 0x7fdef8111eb8>}

print(Car().__dict__)
# {'engine': <__main__.Engine object at 0x7f55c7fb6f28>}
