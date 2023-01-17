#!/usr/bin/python3
'''The Holberton School staff evaluates candidates applying for
a back-end position with multiple technical challenges, like this one:
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

script that takes 2 arguments in order to solve this challenge'''


import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(url)
    if req.status_code == 200:
        for x in req.json()[:10]:
            print("{}: {}".format(
                                  x.get("sha"),
                                  x.get("commit").get("author").get("name")))
    else:
        print("Error code: {}".format(req.status_code))
