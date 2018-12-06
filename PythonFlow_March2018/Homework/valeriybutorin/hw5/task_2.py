"""
- Implement Context Manager which merge two files
  constructor has <path1, path2, mode, new_file_path=None>
  CM has method merge. merge method has optional param (line_numbers=1 - merge line_numbers by line_numbers)
  CM has property new_file_path which returns new file system path
  Use with statement for file merge
  Skip ValueError in __exit__
  log exceptions in __exit__
  handle Exceptions outside CM
- Enjoy MetaClasses and CMs!


P.s Task 1 skipped - has been resolved in past lesson #6
"""

from Homework.valeriybutorin.utils.files_paths import FILE_ONE_PATH, FILE_TWO_PATH, FILE_OUTPUT


class ContextManagerMergeTwoFiles(object):
    def __init__(self, path1, path2, file_output, merge_mode):
        self.__merge_mode = merge_mode
        self.__file_output = open(file_output, "w+")
        self.__file1 = open(path1, "r+")
        self.__file2 = open(path2, "r+")
        self.__file1_lines = []
        self.__file2_lines = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type == ValueError:
            '''AM
            ValueError just printed here but not skipped. 
            '''
            print("Value error has been skipped")
            return True
        print(exc_type)
        print(exc_value)
        print(exc_traceback)
        self.__file1.close()
        self.__file2.close()
        self.__file_output.close()

    def __read_lines(self):
        try:
            for file_1_line, file_2_line in zip(self.__file1.readlines(), self.__file2.readlines()):
                self.__file1_lines.append(file_1_line)
                self.__file2_lines.append(file_2_line)
        except IOError as e:
            print("Something went wrong with reading files: \r\n {0} \r\n {1}".format(self.__file1, self.__file2))
            print(e)

    @staticmethod
    def __grouped(seq, n):
        return zip(*[iter(seq)] * n)

    def merge_files(self):
        self.__read_lines()
        for file1_lines, file2_lines in zip(self.__grouped(self.__file1_lines, self.__merge_mode),
                                            self.__grouped(self.__file2_lines, self.__merge_mode)):
            [self.__file_output.write(l) for l in file1_lines]
            [self.__file_output.write(l) for l in file2_lines]


try:
    with ContextManagerMergeTwoFiles(FILE_ONE_PATH, FILE_TWO_PATH, FILE_OUTPUT, 3) as CmMergeTwoFiles:
        CmMergeTwoFiles.merge_files()
except Exception as io:
    print("Unhandled exception during merging files: \r\n {0} \r\n {1}".format(FILE_ONE_PATH, FILE_TWO_PATH))
    print(io)
