#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Eliminate key value pair from dictionary, contains given key."""
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
