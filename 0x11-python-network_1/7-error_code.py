#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import requests
from sys import argv

if __name__ == '__main__':
    respo = requests.get(argv[1])
    st = respo.status_code
    print(respo.text) if st < 400 else print(
        "Error code: {}".format(respo.status_code))
