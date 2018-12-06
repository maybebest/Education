

"""Request. Session object"""
import requests

with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/from-my/local_machine')

    s.headers.update({'Auth-Token': 'my_auth_token'})

    s.cookies.set(name='locale', value='en-us')

    req = s.get('http://httpbin.org/headers')

    print(req.headers)
    # {'headers':
    #   {'Connection':
    #       'close',
    #       'Auth-Token': 'my_auth_token',
    #       'Cookie': 'locale=en-us; from-my=local_machine',
    #       'Accept-Encoding': 'gzip, deflate',
    #       'Accept': '*/*', 'User-Agent':
    #       'python-requests/2.18.4',
    #       'Host': 'httpbin.org'
    #   }
    # }
