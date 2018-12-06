"""Factory example"""

from _3_factory_abstract_file_writer import AbstractFileWriter
from _4_factory_file_writers import TextFileWriter, BinaryFileWriter


class FileWriterFactory(object):
    file_writers = []

    @classmethod
    def register_writer(self, writer: AbstractFileWriter):
        self.file_writers.append(writer)

    @classmethod
    def get_writer(cls, path, value):
        file_writer = next(
            (io for io in cls.file_writers if type(value) in io.supported_types()), None)

        if not file_writer:
            raise NotImplementedError(
                'File writer for type  "%s" is not implemented' % type(value))

        return file_writer(path, value)


FileWriterFactory.register_writer(BinaryFileWriter)
FileWriterFactory.register_writer(TextFileWriter)

# 'test'.encode() - binary data
writer = FileWriterFactory.get_writer('file_path', 'test'.encode())
writer.write()
