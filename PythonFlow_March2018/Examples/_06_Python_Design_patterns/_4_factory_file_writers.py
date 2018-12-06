import pickle
from _3_factory_abstract_file_writer import AbstractFileWriter


class BinaryFileWriter(AbstractFileWriter):
    @staticmethod
    def mode(): return 'wb+'

    @staticmethod
    def supported_types(): return (dict, tuple, list, bytes, bytearray)

    def _write(self, file, value):
        pickle.dump(value, file)


class TextFileWriter(AbstractFileWriter):
    @staticmethod
    def mode(): return 'w+'

    @staticmethod
    def supported_types(): return (str, int, bool)

    def _write(self, file, value):
        file.write(value)


if __name__ == '__main__':
    writer = TextFileWriter('my_file_path', 'test')
    writer.write()
