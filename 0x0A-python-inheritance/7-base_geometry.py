#!/usr/bin/python3
"""A base geometry class is defined BaseGeometry."""


class BaseGeometry:
    """Base geometry is represented."""

    def area(self):
        """Not put into action."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verify an input parameter integer status.

        Args:
            name (str): The parameter.
            value (int): The input to be verified.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
