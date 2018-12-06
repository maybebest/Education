"""Requests. POST. HTML form"""

import requests


def print_parsed_body(req_body):
    req = requests.post('http://httpbin.org/post', data=req_body)
    res = req.json()
    print(res['form'], res['json'])


print_parsed_body({'lang': 'Python', 'ver': [3]})
# {'lang': 'Python', 'ver': '3'} None

print_parsed_body({'lang': 'Python', 'ver': [2.7, 3.6]})
# {'lang': 'Python', 'ver': ['2.7', '3.6']} None

print_parsed_body([('search_engine', 'google'), ('search_engine', 'yahoo')])
# {'search_engine': ['google', 'yahoo']} None

print_parsed_body('Python')
# {} None

# As we can see in this way we send form-encoded data — much like an HTML form
