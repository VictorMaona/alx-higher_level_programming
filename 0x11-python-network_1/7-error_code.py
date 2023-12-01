#!/usr/bin/python3
"""
script that requests a URL after receiving it,
and presents the response body. If the status code for HTTP is
prints an error message if 400 or more is entered.
makes use of the requests library.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
