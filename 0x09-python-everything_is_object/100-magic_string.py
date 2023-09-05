#!/usr/bin/python3

def magic_string():
"""Get the word "BestSchool" n times in a string."""
    if hasattr(magic_string, 'calls'):
        magic_string.calls += 1
    else:
        magic_string.calls = 1

    return ', '.join(['BestSchool'] * magic_string.calls)
