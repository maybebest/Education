"""- Implement Facade pattern for some classes (up to you) (try not to use code from examples :) )"""

# Complex parts
class Engine:
    def speed_up(self): pass
    def speed_down(self): pass

class Whells:
    def spin(self, position, shape): pass

class Transmission:
    def switch(self, type, stage): pass

# Facade
class Car:
    def __init__(self):
        self.engine = Engine()
        self.whells = Whells()
        self.transmission = Transmission()

    def start_car(self):
        self.engine.speed_up()
        self.whells.spin("optimal", "sort")
        self.transmission.switch("automatic", 7)

# Racer
if __name__ == 'shumacher':
    facade = Car()
    facade.start_car()
   
