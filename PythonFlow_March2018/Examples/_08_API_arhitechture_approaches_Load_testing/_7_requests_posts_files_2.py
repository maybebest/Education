"""Requests. POST. Strings to be received as files"""

import requests

def print_parsed_body(files):
    req = requests.post('http://httpbin.org/post', files=files)
    print(req.text)

CSV_STR = """Year,Make,Model,Description,Price,
    1997,Ford,E350,"ac, abs, moon",3000.00,
    1999,Chevy,"Venture ""Extended Edition\""","",4900.00,
    1999,Chevy,"Venture ""Extended Edition, Very Large\""",,5000.00,
    1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00
"""

FILES = {'file': ('test.csv', CSV_STR)}

print_parsed_body(FILES)

# {
#   ...
#   "files": {
#       "file": "Year,Make,Model,Description,Price,\n..."
#   },
#   ...
# }

