#!/usr/bin/python3
"""defines a function for writing files."""


def write_file(filename="", text=""):
    """Create a UTF8 text file with a string in it.

    Args:
        filename (str): The file name should be written.
        text (str): The document written text.
    Returns:
        The length of the text in characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
