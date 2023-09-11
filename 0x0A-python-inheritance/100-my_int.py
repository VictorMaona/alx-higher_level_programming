#!/usr/bin/python3
"""defines the MyInt class as an inheritor of int."""


class MyInt(int):
    """Invert the!= and == int operators."""

    def __eq__(self, value):
        """with!= behavior, override the == operator."""
        return self.real != value

    def __ne__(self, value):
        """Replace the!= operator with the behavior ==."""
        return self.real == value
