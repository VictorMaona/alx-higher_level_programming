#!/usr/bin/python3


def magic_calculation(a, b):
    """Python function mimic given bytecode behavior.

    Args:
        a (int): The first input value.
        b (int): The second input value.

    Returns:
        Result of calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a

    return result
