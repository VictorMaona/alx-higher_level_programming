#!/usr/bin/python3
"""
script that requests an email address and a URL,
sends the email as a parameter in a POST request to the passed URL,
and lastly presents the response body.
Utilizes the library of requests
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
