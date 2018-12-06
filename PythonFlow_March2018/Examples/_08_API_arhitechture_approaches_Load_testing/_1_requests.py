"""Requests."""

import requests

API_URL = 'http://charity-pets.dev-pro.net/api'

REQ = requests.get('%s/pets' % API_URL)

print('Status: %s, Elapsed: %s' % (REQ.status_code, REQ.elapsed))
# Status: 200, Elapsed: 0:00:00.019993

print(type(REQ.text))  # <class 'str'>

print(type(REQ.content))  # <class 'bytes'>

print(type(REQ.json()))  # <class 'dict'>
