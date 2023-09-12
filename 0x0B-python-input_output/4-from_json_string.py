#!/usr/bin/python3
# 6-from_json_string.py
"""the definition of a JSON-to-object function."""
import json


def from_json_string(my_str):
    """The JSON string Python object representation should be returned."""
    return json.loads(my_str)
