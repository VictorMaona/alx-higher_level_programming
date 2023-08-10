#!/usr/bin/python3
# 2-print_alphabet.py

"""Print lowercase alphabet without new line after each letter."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
