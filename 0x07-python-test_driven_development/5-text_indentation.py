#!/usr/bin/python3
# 5-text_indentation.py
"""Introduces the text-indentation function."""


def text_indentation(text):
    """Each line of text should have two new lines '.', '?', and ':'.

    Args:
        text (string): The text need to print.
    Raises:
        TypeError: If the text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
