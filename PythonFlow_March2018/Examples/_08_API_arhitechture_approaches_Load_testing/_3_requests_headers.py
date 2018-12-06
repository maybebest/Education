"""Requests. Custom headers & Cookies"""

import requests

API_URL = 'http://httpbin.org/headers'

REQ = requests.get(API_URL, headers={
                   'user-agent': 'python_edu_module/0.0.0.1'})
print(REQ.json())
# {
# 'headers': {
#   'Host': 'httpbin.org',
#   'Connection': 'close',
#   'Accept': '*/*',
#   'Accept-Encoding': 'gzip, deflate',
#   'User-Agent': 'python_edu_module/0.0.0.1'
#   }
# }

REQ = requests.get('http://httpbin.org/cookies',
                   cookies={'from-my': 'local_machine'})
print(REQ.text)
# '{"cookies": {"from-my": "local_machine"}}'
