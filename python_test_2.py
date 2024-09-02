"""
This module contains an example function to demonstrate
the usage of docstrings and Pylint error handling.
"""
import os

print(os.getcwd())


def example_function(param1, param2):
    # This function has several issues
    if param1 == param2:
        print("Parameters are equal")
        return True
    else:
        print("Parameters are not equal")
        return False


def main():
    example_function("hello", "world")
    print("This is a test")

    a = 1
    b = 2
    print(a + b)


# This is a comment with no space after the hash
main()
