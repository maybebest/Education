from Homework.valeriybutorin.utils.files_paths import FILE_ONE_PATH, FILE_TWO_PATH, FILE_OUTPUT

"""
- Implement function which merge two files line by line into one new file.
  Empty lines may be skipped (optional, defined by default function arg).
  Retrieve path1, path2, new_filename, skip_empty_lines returns folder system path.
- Handle IOException, and other possible exceptions.
- Use Exception handling.
"""


def remove_empty_from_list(collection):
    '''AM (not for rework)
    it could be written easier:
    return [item for item in collection if item.strip()]
    '''
    return [item for item in collection if item not in ['', "\r\n", "\n"]]

'''AM (not for rework)
"Empty lines may be skipped (optional, defined by default function arg)."
namely "defaulty function arg" - here i meant following function signature
def merge_files(path1, path2, file_output, remove_empty=False):
'''
def merge_files(path1, path2, file_output, remove_empty):
    file_1_lines = []
    file_2_lines = []
    try:
        with open(path1) as file1, open(path2) as file2:
            for file_1_line, file_2_line in zip(file1.readlines(), file2.readlines()):
                file_1_lines.append(file_1_line)
                file_2_lines.append(file_2_line)
    except IOError as io:
        print("Something went wrong with reading files: \r\n {0} \r\n {1}".format(path1, path2))
        print(io)
    except Exception as io:
        print("Unhandled exception during reading files: \r\n {0} \r\n {1}".format(path1, path2))
        print(io)

    if remove_empty:
        file_1_lines = remove_empty_from_list(file_1_lines)
        file_2_lines = remove_empty_from_list(file_2_lines)

    try:
        with open(file_output, "w") as result:
            for file1_line, file2_line in zip(file_1_lines, file_2_lines):
                result.write(file1_line)
                result.write(file2_line)
    except IOError as io:
        print("Something went wrong while lines are writing to the file: {0}".format(file_output))
        print(io)
    except Exception as e:
        print("Unhandled exception while lines are writing to the file: {0}".format(file_output))
        print(e)


merge_files(FILE_ONE_PATH, FILE_TWO_PATH, FILE_OUTPUT, remove_empty=True)
