"""Requests. Python scripts aren't affected by CORS."""

import requests

RES = requests.options(
    'https://images.apple.com/v/home/dn/built/styles/main.built.css')

print(RES.headers.get('allow'), RES.headers.get('Access-Control-Allow-Origin'))
# GET,HEAD,POST,OPTIONS https://www.apple.com

RES = requests.get(
    'https://images.apple.com/v/home/dn/built/styles/main.built.css')

print(RES.headers)
#{'Set-Cookie': 'geo=UA; path=/; domain=.apple.com', 'Cache-Control': 'max-age=239',
# 'Access-Control-Allow-Origin': 'https://www.apple.com', 'Content-Length': '20245',
# 'Vary': 'Accept-Encoding', 'Server': 'Apache', 'Connection': 'keep-alive',
# 'Content-Type': 'text/css', 'Content-Encoding': 'gzip'}

print(RES.request.headers)
#{'User-Agent': 'python-requests/2.18.4', 'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive'}

REQ = requests.delete(
    'https://images.apple.com/v/home/dn/built/styles/main.built.css')

REQ.raise_for_status()
# requests.exceptions.HTTPError: 501 Server Error: Not Implemented for url
