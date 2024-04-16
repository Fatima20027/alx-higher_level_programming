#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """module write_file"""
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(text)
        return len(text)
