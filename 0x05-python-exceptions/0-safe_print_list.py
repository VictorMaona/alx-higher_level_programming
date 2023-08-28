#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x elements of a list and an integer.

    Args:
        my_list (list): The list of items to print.
        x (int): items from my_list should be printed.

    Returns:
        shows how many elements there are.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
