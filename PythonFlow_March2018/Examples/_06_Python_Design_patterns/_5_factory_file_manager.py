"""Factory example"""

from _3_factory_abstract_file_writer import AbstractFileWriter
from _4_factory_file_writers import TextFileWriter, BinaryFileWriter


class FileManager(object):
    file_writers = []

    @classmethod
    def register_writer(self, writer: AbstractFileWriter):
        self.file_writers.append(writer)

    @classmethod
    def write(cls, path, value):
        file_writer = next(
            (io for io in cls.file_writers if type(value) in io.supported_types()), None)

        if not file_writer:
            raise NotImplementedError(
                'File writer for type  "%s" is not implemented' % type(value))

        file_writer(path, value).write()


FileManager.register_writer(BinaryFileWriter)
FileManager.register_writer(TextFileWriter)

# 'test'.encode() - binary data
FileManager.write('file_path', 'test'.encode())
