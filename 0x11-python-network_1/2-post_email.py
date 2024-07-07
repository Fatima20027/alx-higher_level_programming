#!/usr/bin/python3
""" Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response"""

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2].encode('utf-8')

req = urllib.request.Request(url, data=email, method='POST')
with urllib.request.urlopen(req) as r:
    response = r.read().decode('utf-8')
    print("Your email is: {}".format(response))
