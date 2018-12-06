'''
# Homework 3 ##
- Implement function which merges two files line by line into one new file.
  Empty lines may be skipped (optional, defined by default function arg).
  Receives path1, path2, new_filename, skip_empty_lines returns folder system path.
- Handle IOException, and other possible exceptions.
- Use Exception handling.
'''

import os

DIR = os.getcwd()
f1 = (DIR+"\\task2_file1.txt")
f2 = (DIR+"\\task2_file2.txt")
res = (DIR+"\\task2_result.txt")


def is_blank_line(line):
    '''SZ There is a better way to check whether line empty or not

        return not str.strip()

        method "strip" returns string without space characters and characters like \n and \r
    '''

    if line == "\n" or "":
        return True


def append_to_file(file, string):
    with open(file, "a+") as FILE:
        FILE.write(string)


def has_more_lines(file1, file2):
    '''SZ
        Please use "with" statement. It is possible to open more than one file with it

        with open(file1) as first, open(file2) as second:
            pass
    '''

    first = open(file1)
    second = open(file2)
    counter1 = 0
    counter2 = 0

    '''SZ there is a better way to get lines count in a file
        first_file_lines_count = len(first.readlines())
    '''

    for g in first:
        counter1 += 1
    for h in second:
        counter2 += 1
    first.close()
    second.close()
    return counter1 > counter2


def merge(file1, file2, result):
    '''SZ Please use "with" construction in purpose to open files'''

    f1 = open(file1)
    f2 = open(file2)
    f3 = open(result, "w+")

    '''SZ there is much better way to get content from multiple file and compare it

        result = [(line_1, line_2) for line_1 in f1 for line_2 in f2]

        It generates list of tuples with lines from first and second file
    '''

    while True:
        line1 = f1.readline()
        line2 = f2.readline()

        '''SZ Method "readline" returns a string, there is no need in additional conversion'''

        string = (str(line1)+str(line2))
        '''AM
        f3 is not used.
        '''
        append_to_file(result, string)
        if not line1:
            break

    f1.close()
    f2.close()
    f3.close()


def merge_no_empty(file1, file2, result):
    f1 = open(file1)
    f2 = open(file2)
    f3 = open(result, "w+")

    '''SZ there is much better way to get content from multiple file and compare it

        result = [(line_1, line_2) for line_1 in f1 for line_2 in f2]

        It generates list of tuples with lines from first and second file
    '''

    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if not is_blank_line(line1):
            append_to_file(result, line1)
        if not is_blank_line(line2):
            append_to_file(result, line2)
        if not line1:
            break

    f1.close()
    f2.close()
    f3.close()


def merger(file1, file2, result, skip_empty=False):
    '''AM
    Too complicated and to many conditional logic.
    It is very hard to cover such function with tests :)
    Please rewrite your merger in something like that
    with open(file1) as f1, open(file2) as f2, open(result) as res,
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        if skip:
            lines1 = list(filter(lambda line: not is_blank_line(line), lines1))[::-1]
            lines2 = list(filter(lambda line: not is_blank_line(line), lines2))[::-1]            
        while True:
            line1 = lines1.pop() if lines1 else None
            line2 = lines2.pop() if lines2 else None            

            if not line1 and line2:
                break

            if line1:
                res.write(line1)
            
            if line2:
                res.write(line2)
    '''
    try:
        if has_more_lines(file1, file2):
            if skip_empty:
                merge_no_empty(file1, file2, result)
            else:
                merge(file1, file2, result)
        else:
            if skip_empty:
                merge_no_empty(file2, file1, result)
            else:
                merge(file2, file1, result)
    except IOError as io:
        print(io)
    else:
        return DIR


#print(merger(f1, f2, res))
#print(merger(f1, f2, res, skip_empty=True))