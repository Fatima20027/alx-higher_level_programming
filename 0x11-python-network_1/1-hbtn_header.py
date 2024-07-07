#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    respo = urllib.request.Request(url)
    with urllib.request.urlopen(respo) as r:
        print(dict(r.headers).get("X-Request-Id"))
