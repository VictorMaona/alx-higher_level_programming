#!/usr/bin/python3
"""defines a function for insertion of text files."""


def append_after(filename="", search_string="", new_string=""):
    """Add text to file after each line that contains specified string.

    Args:
        filename (str): The name of file.
        search_string (str): The string to search in file.
        new_string (str): The string to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
