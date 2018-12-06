
# Homework 3 ##
"""- Implement function which copying only duplication lines from one file two other.
  Retrieve path1, path2, new_filename, returns folder system path."""

""""- Handle IOException, and other possible exceptions.
- Use Exception handling."""
import os

File1 = os.getcwd() + "\\test.txt"
File2 = os.getcwd() + "\\shest.txt"
File3 = os.getcwd() + "\\new_file.txt"

def copy_duplication_lines(path1, path2, file_result):
    '''AM
    Too many nesting levels. Please use following construction
    with open(path1) as first, open(path2) as second, open(path3) as third:
        #do something
    '''
    with open(path1, 'r+') as first:
        with open(path2, 'r') as second:
            with open(file_result, 'r+') as result:
                try:
                    for line in first:
                        if line in second:
                            result.write(line)
                        if len(line.strip()) == 0:
                            result.write('\n')
                except IOError:
                    print("Problem with lines writing")


copy_duplication_lines(File1, File2, File3)



