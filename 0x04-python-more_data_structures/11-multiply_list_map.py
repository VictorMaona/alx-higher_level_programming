#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Make fresh list of components with a 2 multiplier."""
    return (list(map((lambda i: i * number), my_list)))
