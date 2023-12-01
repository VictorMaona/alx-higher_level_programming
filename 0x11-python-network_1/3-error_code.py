#!/usr/bin/python3
"""
A script that accepts a URL and sends a request to that URL,
and presents the reply body (decoded in utf-8).
deals with urllib.error. HTTP status code printed along with HTTPError exceptions.
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
