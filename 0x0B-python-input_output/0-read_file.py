#!/usr/bin/python3
"""Creates a method that reads text files."""


def read_file(filename=""):
    """To print UTF8 text file contents use stdout command."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
