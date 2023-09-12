#!/usr/bin/python3
"""makes a string to-JSON function definition."""
import json


def to_json_string(my_obj):
    """Return a string object JSON representation."""
    return json.dumps(my_obj)
