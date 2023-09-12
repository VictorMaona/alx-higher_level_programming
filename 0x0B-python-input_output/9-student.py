#!/usr/bin/python3
"""Students specify a class."""


class Student:
    """the student voice."""

    def __init__(self, first_name, last_name, age):
        """Create a fresh Student.

        Args:
            first_name (str): The student name in the first.
            last_name (str): The student last name.
            age (int): the student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get definition of Student in a dictionary."""
        return self.__dict__
