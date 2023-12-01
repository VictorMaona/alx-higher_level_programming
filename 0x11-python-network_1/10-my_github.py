#!/usr/bin/python3
"""
A script that requests the (username and personal access token) from GitHub,
accesses information using personal access token in conjunction with Basic Authentication,
and shows your user ID on GitHub.
makes use of requests library
"""
import sys
import requests
from requests.auth import HTTPBasicAuth
