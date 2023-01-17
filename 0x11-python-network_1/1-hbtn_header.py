#!/usr/bin/python3
'''displays the value of  X-Request-Id variable in the header of response'''


import sys
import urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(dict(response.headers).get('X-Request-Id'))
