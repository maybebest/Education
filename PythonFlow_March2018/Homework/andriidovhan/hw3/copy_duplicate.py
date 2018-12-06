import os

def copy_duplicate(file_1, file_2, new_file):
    '''AM
    Opening file_2 is not covered by exception handling
    Also it could be written simplier
    try:
        with open(file_1, 'r') as file_11, open(file_2, 'r') as file_22:
            pass #do something
    except IOError as err:
        print(err)
    '''
    try:
        with open(file_1, 'r') as file1, open(file_2, 'r') as file2:
            content_file_1 = [row.strip() for row in file1]
            content_file_2 = [row.strip() for row in file2]
    except IOError:
        print('file is not found')
    
    '''AM
    Variables could be declared with empty before assigning value
    f.e. 
    array_1 = None
    array_1 = []
    ...
    Also please use variable names with some meaning
    '''
    try:
        dubicate_lines = list(set(content_file_1) & set(content_file_2))
    except UnboundLocalError:
        print('something went wrong. please, make sure you have passed corect file')

    with open(new_file, 'w+') as file_3:
        for l in dubicate_lines:
            file_3.write("{} \n".format(l))
        try:
            print('New file is created in the following folder: "{}"'.format(os.path.dirname(os.path.realpath(__file__))))
        except NameError:
            print('looks like you forgot to import "OS"')
        

try:
    copy_duplicate('test_file_1', 'test_file_2', 'file_with_duplicate')
except NameError as error:
    print(error)
except TypeError:
    print(error)
    print('looks like function is invoked incorrecty(SyntaxError)')
