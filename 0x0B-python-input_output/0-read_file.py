#!/usr/bin/python3
""" function that reads a text file"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as file:
        """prints it to stdout"""
        print(file.read())
