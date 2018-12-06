"""
- Implement function which copying only duplication lines from one file two other.
  Retrieve path1, path2, new_filename, returns folder system path.
"""
from Homework.valeriybutorin.utils.files_paths import FILE_ONE_PATH, FILE_TWO_PATH, FILE_OUTPUT


def copy_duplicate_lines(path1, path2, file_output):
    file_1_lines = []
    file_2_lines = []
    with open(path1) as file1, open(path2) as file2:
        for file_1_line, file_2_line in zip(file1.readlines(), file2.readlines()):
            file_1_lines.append(file_1_line)
            file_2_lines.append(file_2_line)

    with open(file_output, "w") as result:
        result.writelines(set([line for line in file_2_lines if line in file_1_lines]))


copy_duplicate_lines(FILE_ONE_PATH, FILE_TWO_PATH, FILE_OUTPUT)
