#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print numbers from 1 to 100 with gap between each.

    Print Fizz instead of the number when it is multiple of three.
    Print Buzz instead of the number when it is multiple of five.
    Print FizzBuzz rather number for multiples of three and five.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
