"""
This module contains an example function to demonstrate
the usage of docstrings and Pylint error handling.
"""

import os

print(os.getcwd())


def example_function(param1, param2):
    """
    This function compares two prints to check if they are equal.

    Args:
        print1 (type): Description of print1.
        print2 (type): Description of print2.

    Returns:
        bool: True if the prints are equal, False otherwise.
    """

    if param1 == param2:
        print("Parameters are equal")
        return True

    print("Parameters are not equal")
    return False


def main():
    """
    This is the main function that will call the example function
    """

    example_function("hello", "world")
    print("This is a test")

    a = 1
    b = 2
    print(a + b)


# This is a comment with no space after the hash
main()
