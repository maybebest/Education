"""
- Implement function which merge two files line by line into one new file.
  Empty lines may be skipped (optional, defined by default function arg).
  Retrieve path1, path2, new_filename, skip_empty_lines returns folder system path.
- Handle IOException, and other possible exceptions.
- Use Exception handling.
- Enjoy!
"""
from itertools import zip_longest


def merge_by_line(path1, path2, new_filename, skip_empty_lines=None):
    try:
        with open(path1, 'r') as file_1, open(path2, 'r') as file_2:
            '''AM (not for rework)
            Also could be written in this way
            f1 = [x for x in file_1 if x.strip()] if skip_empty_lines else file_1.readlines()
            '''
            f1 = [x for x in file_1 if (x.strip() and skip_empty_lines) or not skip_empty_lines]
            f2 = [x for x in file_2 if (x.strip() and skip_empty_lines) or not skip_empty_lines]
            merged = [x for x in zip_longest(f1, f2)]
        with open(new_filename, 'w') as new_file:
            to_write = []
            for x, y in merged:
                to_write.append(x) if x else None
                to_write.append(y) if y else None
            new_file.write(''.join(to_write))
    except (IOError, ValueError, TypeError) as e:
        print("Error occurred! Message: '{}'".format(e))


# merge_by_line("test_data", "test_data_2", "task_2_new_file", False)
merge_by_line("test_data", "test_data_2", "task_2_merged_file", True)
