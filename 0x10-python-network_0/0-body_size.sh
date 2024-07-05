#!/bin/bash
# Get length of body of a request

curl -s "$1" | wc -c
