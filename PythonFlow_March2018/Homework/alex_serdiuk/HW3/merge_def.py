
""""- Implement function which merge two files line by line into one new file.
  Empty lines may be skipped (optional, defined by default function arg).
  Retrieve path1, path2, new_filename, skip_empty_lines returns folder system path."""

import os

File1 = os.getcwd() + "\\test.txt"
File2 = os.getcwd() + "\\shest.txt"
File4 = os.getcwd() + "\\new_file2.txt"

'''AM
Requirement is not impelmented:
"Empty lines may be skipped (optional, defined by default function arg)."
Expected function signature
def merge_lines(path1, path2, file_result, skip_empty_lines=True):
    pass
Also i should be able to skip empty line
'''
def merge_lines(path1, path2, file_result):

    '''AM
    Please use following construction here
    with open(path1, 'r') as first, open(path2, 'r') as second:
        #do something
    '''
    with open(path1, 'r') as first:
        f = first.readlines()

    with open(path2, 'r') as second:
        s = second.readlines()

    result = []
    m = max([len(f), len(s)])
    try:
        for i in range(0, m):
            if i < len(f) and f[i].strip():
                result.append(f[i].rstrip('\n'))
            if i < len(s) and s[i].strip():
                result.append(s[i].rstrip('\n'))
        with open(file_result, 'r+') as r:
            r.write(str(result))
    except IOError:
        print("Problem with lines merge")

    print(result)

merge_lines(File1, File2, File4)
