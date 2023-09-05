#!/usr/bin/python3
"""class having a set amount of slots."""


class LockedClass:
    """
    Stop the user from creating brand new LockedClass attributes.
    anything else than qualities known 'first_name'.
    """

    __slots__ = ["first_name"]
