#!/usr/bin/python3
''' script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''


import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    name, token = sys.argv[1], sys.argv[2]
    tuple_crd = (name, token)
    response = requests.get(url, auth=tuple_crd)
    response = response.json()
    print(response.get('id'))
