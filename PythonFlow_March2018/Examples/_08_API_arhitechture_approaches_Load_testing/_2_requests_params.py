"""Requests. Passing params"""

import requests

API_URL = 'http://charity-pets.dev-pro.net/api'

REQ = requests.get('%s/pets' % API_URL, params={'type': 'Dog', 'limit': 1})

print(REQ.headers)
print(REQ.url)
# http://charity-pets.dev-pro.net/api/pets?type=Dog&limit=1

RES = REQ.json()

PET = RES.get('petsData')[0]

print(PET.get('type'))  # Dog
