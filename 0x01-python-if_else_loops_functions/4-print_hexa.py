#!/usr/bin/python3
# 4-print_hexa.py

"""Print decimal and hexadecimal values of 0 to 98."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
