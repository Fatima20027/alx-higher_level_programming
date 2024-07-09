#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]

        with urllib.request.urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
