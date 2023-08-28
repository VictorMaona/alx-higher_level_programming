#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """safe operation of function.

    Args:
        fct: The action to be taken.
        args: Defenses of the fct.

    Returns:
        In the event of a mistake none.
        If not the outcome of the fct call.
    """
    try:
        result = fct(*args)
        return result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
