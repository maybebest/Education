"""Requests. POST. JSON"""

import requests
import json


def print_parsed_body(req_body):
    #req = requests.post('http://httpbin.org/post', json=req_body)
    req = requests.post('http://httpbin.org/post', data=json.dumps(req_body))
    res = req.json()
    print(res['form'], res['json'])


print_parsed_body({'lang': 'Python', 'ver': [3]})
# {} {'ver': [3], 'lang': 'Python'}

print_parsed_body({'lang': 'Python', 'ver': [2.7, 3.6]})
# {} {'ver': [2.7, 3.6], 'lang': 'Python'}

print_parsed_body([('search_engine', 'google'), ('search_engine', 'yahoo')])
# {} [['search_engine', 'google'], ['search_engine', 'yahoo']]

print_parsed_body('Python')
# {} Python
