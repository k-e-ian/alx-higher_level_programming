#!/usr/bin/python3
'''script that takes URL, sends request URL, displays value var X-Request-Id'''


import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
