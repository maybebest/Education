"""Requests. Response status codes"""

import requests

REQ = requests.get('http://httpbin.org/status/500')  # bad req

print(REQ.status_code == requests.codes.ok)  # False

print(REQ.status_code == requests.codes.internal_server_error)  # True

print(REQ.status_code == requests.codes.not_found)  # False

