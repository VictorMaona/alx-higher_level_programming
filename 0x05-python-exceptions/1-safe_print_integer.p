#!/usr/bin/python3


def safe_print_integer(value):
    """Function prints an integer.

    Args:
        value (int): The printable integer.

    Returns:
        False if a TypeError or ValueError happens.
        If not, then true.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
