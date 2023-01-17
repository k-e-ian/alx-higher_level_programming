#!/usr/bin/python3
''' script that fetches https://alx-intranet.hbtn.io/status '''


import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    the_body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(the_body)))
    print("\t- content: {}".format(the_body))
    print("\t- utf8 content: {}".format(the_body.decode("utf-8")))
