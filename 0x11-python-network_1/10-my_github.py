#!/usr/bin/python3
"""
A script that requests the (username and personal access token) from GitHub,
accesses information using personal access token in conjunction with Basic Authentication,
and shows your user ID on GitHub.
makes use of requests library
"""

import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]

    # Describe user information endpoint for GitHub API.
    url = 'https://api.github.com/user'

    # Utilize personal access token to configure Basic Authentication.
    auth = (username, password)

    # Sends the GitHub API a GET request.
    response = requests.get(url, auth=auth)

    # Verify whether the request was fulfilled.
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print(None)
else:
    print("Usage: ./10-my_github.py <VictorMaona> <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
>")
