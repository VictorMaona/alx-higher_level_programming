#!/usr/bin/python3
"""defines a function for adding files."""


def append_write(filename="", text=""):
    """adds a string to a UTF8 text file end.

    Args:
        filename (str): The file name that will be appended.
        text (str): The string that will be added to the file.
    Returns:
        how many characters are added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
