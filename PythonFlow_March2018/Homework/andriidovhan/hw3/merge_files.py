import os

def write_to_file(new_file, array_with_lines):
    with open(new_file, 'w+') as f:
        for l in array_with_lines:
            f.write(l)
        try:
            print('New file is created in the following folder: "{}"'.format(os.path.dirname(os.path.realpath(__file__))))
        except NameError:
            print('looks like you forgot to import "OS"')

def get_lines(file, skip_empty_lines):
    return [line for line in file if line.strip()] if skip_empty_lines else file.readlines()

def merge_two_files(file_1, file_2, new_file, skip_empty_lines=True):
    # filenames = [file_1, file_2]
    try:
        with open(file_1) as file1, open(file_2) as file2:
            lines1 = get_lines(file1, skip_empty_lines)
            lines2 = get_lines(file2, skip_empty_lines)
    except IOError:
        print('oops, file is not found')

    try:    
        with open(new_file, "w") as output_file:
            for line_from_file_1, line_from_file_2 in zip(lines1, lines2):
                output_file.write(line_from_file_1)
                output_file.write(line_from_file_2)
    except IOError as err:
        print(err)
    '''AM
    Too many nesting levels. 
    Please use following construction here:
    with open(file_1, 'w+') as file1, open(file_2, 'w+') as file1, open(new_file, 'w+') as outfile:
        do something        
    '''
    
    '''AM 2
    "- Implement function which merge two files line by line into one new file."
    Files should be merged line by line
    Please use following algorithm here:
    
    def get_lines(file, skip_empty):
        return [line for line in file if line.strip()] if skip_empty else file.readlines()

    try:
        with open(file_1) as file1, open(file_2) as file2:
            lines1 = get_lines(file1, skip_emty_lines)
            lines2 = get_lines(file2, skip_emty_lines)            
    except IOError:
        # do something
    else:
        with open(res_file_path) as res_file:
            while True:
                line1 = lines1.pop(0) if lines1 else None
                line2 = lines2.pop(0) if lines2 else None

                if line1 == None and line2 == None
                    break
                if line1:                        
                    res_file.write(line1)
                if line2:
                    res_file.write(line2)
    '''
    # outfile = []
    # for fname in filenames:
    #     with open(fname) as infile:
    #         for line in infile:
    #             if skip_emty_lines:
    #                 if line.strip():
    #                     outfile.append(line)
    #             else:
    #                 outfile.append(line)

    # write_to_file(new_file, outfile)
    # try:
    #     with open(new_file, 'w+') as outfile:
    #         for fname in filenames:
    #             with open(fname) as infile:
    #                 for line in infile:
    #                     if skip_emty_lines:
    #                         # if not len(line)==1:
    #                         '''AM (not for rework)
    #                         it could be written easier
    #                         if line.strip():
    #                             outfile.write(line)
    #                         '''
    #                         if line not in ['\n', '\r\n']:
    #                             outfile.write(line)
    #                     else:
    #                         outfile.write(line)
    # except IOError:
    #     print('some file is not found')
    #     exit(1)

try:
    merge_two_files('test_file_1', 'test_file_2', 'file_after_merge')
except NameError as error:
    print(error)
except TypeError:
    print(error)
    print('looks like function is invoked incorrecty(SyntaxError)')
