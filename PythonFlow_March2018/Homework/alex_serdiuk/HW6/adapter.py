"""- Implement Adapter pattern for some classes (up to you)"""

'''AM
Please se interface examples in presentation.
I should be unable to create instance of an interface:
class ICM(ABC):
    @abstractmethod
    def __enter__(self):
        pass
    @abstractmethod
    def __exit__(self):
        pass
'''
# Adaptee interface
class EuropeanPensionerInterface:
    def men(self): pass
    def women(self): pass


# Adaptee
class Pensioner(EuropeanPensionerInterface):
    def men(self):
        return 55

    def women(self):
        return 50


# Target interface
class UkranianPensionerInterface:
    def men(self): pass
    def women(self): pass


# The Adapter
class Adapter(UkranianPensionerInterface):
    __pensioner = None

    def __init__(self, pensioner):
        self.__pensioner = pensioner

    def men(self):
        return 60

    def women(self):
        return self.__pensioner.women()

'''AM 
How can i use this Adapter?
Please add some tests to understand Adapter functionality
'''