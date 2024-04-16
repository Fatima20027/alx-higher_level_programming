#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
 using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """module save_to_json_file
    accepts Python object and sends JSON representation to file"""

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
        return len(json.dumps(my_obj))
