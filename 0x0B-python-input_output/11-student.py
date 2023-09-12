#!/usr/bin/python3
"""Student defines a class."""


class Student:
    """present a student."""

    def __init__(self, first_name, last_name, age):
        """Create a fresh Student..

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of the student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a definition of the Student in a dictionary.

        represents only those characteristics that are present
        in the list if attrs is a list of strings.

        Args:
            attrs (list): (Optional) Qualities must be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Change all of the Student characteristics.

        Args:
            json (dict): Primary value pairs to use in place of attributes.
        """
        for k, v in json.items():
            setattr(self, k, v)
