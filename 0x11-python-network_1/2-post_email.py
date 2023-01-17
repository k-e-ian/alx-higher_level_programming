#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as param'''


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
