import os

print('Current directory:', os.getcwd())


def duplicate_lines(path1, path2, res):
    try:
        with open(path1, 'r+') as file1:
            '''AM
            Extra comprehension here
            file1.readlines() returns list            
            '''
            lines1 = file1.readlines()
        '''AM
        Too many nesting levels, please use following construction
        with open(path1) as file1, open(path2) as file2:
            #do something with file1, file2
        '''
        with open(path2, 'r+') as file2, open(res, 'w+') as res_file:
            for i in file2.readlines():
                if i in lines1:
                    res_file.write(i)
    except FileNotFoundError as err:
        print('==={0}==='.format(err))
    except IOError as err:
        print('Writing to file FAILED', err, err.args)
    else:
        return os.path.abspath(os.path.dirname(res_file.name))


print('Path to result file:', duplicate_lines('file1', 'file2', 'duplicates_file'))
