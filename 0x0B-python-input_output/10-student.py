#!/usr/bin/python3
"""Student defines a class."""


class Student:
    """portray a student."""

    def __init__(self, first_name, last_name, age):
        """Create a fresh Student.

        Args:
            first_name (str): The student first name.
            last_name (str): The student last name.
            age (int): How old the student is as age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a definition of the Student in a dictionary.

        represents only those characteristics that are
        present in the list if attrs is a list of strings.

        Args:
            attrs (list): (Optional) The qualities must be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict_
