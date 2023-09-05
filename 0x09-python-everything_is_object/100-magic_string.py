#!/usr/bin/python3
def magic_string():
    # Attributes are possible for function objects, the global number of calls
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
