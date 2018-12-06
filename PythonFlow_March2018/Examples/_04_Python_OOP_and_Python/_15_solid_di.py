"""SOLID. Without DIP"""


class Engine(object):
    pass


class Tires(object):
    pass


class Car(object):
    def __init__(self):
        self.engine = Engine()
        self.tires = Tires()

    def drive(self):
        print('Driving')


my_new_car = Car()
my_new_car.drive()
