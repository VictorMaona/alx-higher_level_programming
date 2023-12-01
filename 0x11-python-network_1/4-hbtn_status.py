#!/usr/bin/python3
"""
Script that retrieves the status from  https://alx-intranet.hbtn.io/status
makes use of the requests library
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
