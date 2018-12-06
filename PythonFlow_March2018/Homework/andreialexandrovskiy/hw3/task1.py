'''
# Homework 3 ##
- Implement a function that copies duplicate lines from one file to another.
  Receives path1, path2, new_filename, returns folder system path.
- Handle IOException, and other possible exceptions.
- Use Exception handling.
'''

import os

DIR = (os.getcwd())
file1 = (DIR+"\\task1_file1.txt")
file2 = (DIR+"\\task1_file2.txt")
result = (DIR+"\\task1_result.txt")


def append_to_file(file, string):
    with open(file, "a+") as FILE:
        FILE.write(string)
        FILE.write("\n")


def search_for_line(file, line):
    with open(file) as FILE:
        for string in FILE:
            if string == line:
                return True


def duplicate_lines_to_file(f1, f2, result):
    try:
        with open(f1) as FILE1:
            '''SZ 
                Not used variable FILE2, also it is possible to open more that one file with construction "with"
                with open(f1) as FILE1, open(f2) as FILE2:
                    pass
            '''
            with open(f2) as FILE2:
                for line in FILE1:
                    '''AM
                    Also it is a bad idea to open file in each iteration. 
                    Please read lines from file once and then manipulate with result
                    '''
                    if search_for_line(f2, line):
                        append_to_file(result, line)
    except IOError as io:
        print(io)
    else:
        return DIR


print(duplicate_lines_to_file(file1, file2, result))

