#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print out the first x integer entries of a list.

    Args:
        my_list (list): The list of items to print.
        x (int): items from my_list should be printed.

    Returns:
        The quantity of printed elements.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
