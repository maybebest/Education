"""Singleton example"""

from _1_Ilogger import ILogger
from datetime import datetime


class PrintLogger(ILogger):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PrintLogger, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def info(self, value):
        print(self.__format_str(value))

    def warn(self, value):
        print(self.__format_str('Warning! %s' % value))

    def error(self, value):
        print(self.__format_str('Error! %s' % value))

    def __get_time(self):
        return datetime.now().time()

    def __format_str(self, value):
        return '%s: %s' % (self.__get_time(), value)


print(PrintLogger() is PrintLogger())  # True
print(id(PrintLogger()))  # 139978691887960
print(id(PrintLogger()))  # 139978691887960

logger = PrintLogger()
logger.info('print info')
logger.warn('print warning')
try:
    raise ValueError('Test Value Error')
except ValueError as er:
    logger.error(er)
