#!/usr/bin/python3
""" function that reads a text file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    Returns none
    """

    with open(filename, encoding="UTF8") as file:
        print(file.read(), end="")
