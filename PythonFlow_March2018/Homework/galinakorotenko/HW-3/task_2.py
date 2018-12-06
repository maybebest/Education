"""
Implement function which merge two files line by line into one new file.
  Empty lines may be skipped (optional, defined by default function arg).
  Retrieve path1, path2, new_filename, skip_empty_lines returns folder system path.
"""
import os


def file_merging(file_1, file_2, file_output, flag):
    filenames = [file_1,  file_2]
    '''AM
    Too many nesting levels
    Please use following construction
    with open(file_output, 'w') as outfile, with open(file_1) as f1, with open(file_2) as f2:
        #do something
    '''
    try:
        with open(file_output, 'w') as outfile:
            for fname in filenames:
                try:
                    with open(fname) as infile:
                        for line in infile:
                            if flag:
                                # Script considers all lines are not empty.
                                # I do not understand why. Please advice
                                if line:
                                    outfile.write(line)
                            else:
                                outfile.write(line)
                except IOError:
                     print('An error occured trying to open the initial files')
    except IOError:
        print('An error occured trying to open result file.')


    my_path = os.path.realpath(__file__)
    return my_path


path = file_merging('file_1', 'file_2', 'merged_file', flag=True)
print(path)
