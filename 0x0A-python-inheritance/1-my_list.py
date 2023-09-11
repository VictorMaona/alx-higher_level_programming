#!/usr/bin/python3
"""definition of an inherited list class MyList."""


class MyList(list):
    """gives the built-in list class sorted printing support."""

    def print_sorted(self):
        """Create a list that is sorted ascending."""
        print(sorted(self))
