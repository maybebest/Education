"""Requests. POST. Files"""

import requests

def print_parsed_body(files):
    req = requests.post('http://httpbin.org/post', files=files)
    print(req.text)

print_parsed_body({'file': open('_test.xlsx', 'rb')})

print_parsed_body([('file1', open('_test.xlsx', 'rb')),
                   ('file2', open('the_Zen_of_Python', 'r'))])

print_parsed_body({'file3': open('_test.xlsx', 'rb'),
                   'file4': open('the_Zen_of_Python', 'r')})
# {
#   ...
#   "files": {
#       "file3": "<binary data>"
#       "file4": "<text data>"
#   },
#   ...
# }
