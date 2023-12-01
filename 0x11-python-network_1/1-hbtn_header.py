#!/usr/bin/python3
"""
script that requests a URL after receiving it,
shows the X-Request-Id variable's value in the header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
