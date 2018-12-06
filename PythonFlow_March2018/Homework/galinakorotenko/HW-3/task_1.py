"""
Implement function which copying only duplication lines from one file to other.
Retrieve path1, path2, new_filename, returns folder system path.
"""
import os


def collect_lines(file_name):
    """
    Function to open file with file_name and
    collect all lines into list of string
    Return: list
    """
    new_list = []
    try:
        with open(file_name) as my_file:
            '''AM
            It could be written easier
            Please use readlines method
            '''
            for line in my_file:
                if line:
                    new_list.append(str(line.rstrip()))
                    '''AM
                    Extra if here:
                    if line:
                        ...
                        if not line:
                            # code here won't be executed
                    '''
                    if not line:
                        break
                else:
                    pass
    except IOError:
        print('An error occured trying to read the file.')
    return new_list


def find_duplicates(file_1, file_2, new_file):

    list_1 = collect_lines(file_1)
    list_2 = collect_lines(file_2)
    result = set(list_1).intersection(set(list_2))
    try:
        with open(new_file, 'w+') as new_file:
            for elem in result:
                if elem:
                    new_file.write(elem + '\n')
    except IOError:
        print('An error occured trying to read the file.')
    my_path = os.path.realpath(__file__)
    return my_path


path = find_duplicates('file_1', 'file_2', 'new_file')

print(path)