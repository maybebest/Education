"""SOLID. With DIP"""


class IEngine(object):
    def add_gas(self):
        raise NotImplementedError('add_gas is not implemented')


class DieselEngine(IEngine):
    def add_gas(self):
        print('Add diesel')


class GasolineEngine(IEngine):
    def add_gas(self):
        print('Add gasoline')


class Car(object):
    def __init__(self, engine: IEngine):
        self.engine = engine

    def drive(self):
        self.engine.add_gas()


my_new_car = Car(DieselEngine())
my_new_car.drive()  # Add diesel
my_new_car2 = Car(GasolineEngine())
my_new_car2.drive()  # Add gasoline
