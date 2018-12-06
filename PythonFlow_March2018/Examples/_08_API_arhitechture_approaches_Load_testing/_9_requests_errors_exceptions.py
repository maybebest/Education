"""Errors and Exceptions"""
import requests

try:
    #REQ = requests.get('http://httpbin.org/status/500',  timeout=0.001)
    REQ = requests.get('http://httpbin.org/status/500')
    REQ.raise_for_status()

except requests.exceptions.Timeout as ex:
    print('Timeout:', ex)
    # Timeout: ... 'Connection to httpbin.org timed out. (connect timeout=0.001)'

except requests.exceptions.ConnectionError as ex:
    print('ConnectionError:', ex)
    # ConnectionError: ...Failed to establish a new connection...

except requests.exceptions.HTTPError as ex:
    print('HTTPError, status: ', ex.response.status_code)
    # HTTPError, status:  500

except requests.exceptions.RequestException as ex:
    print('RequestException:', ex)

except Exception as ex:
    print('Exception:', ex)

