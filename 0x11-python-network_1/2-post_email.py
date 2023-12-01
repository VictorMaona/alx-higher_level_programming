#!/usr/bin/python3
"""
An email and a URL are entered into the script,
sends a POST request with the email parameter to the passed URL,
shows the response body (decoded in utf-8) and email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
