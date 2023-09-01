#!/usr/bin/python3
"""
This script takes a URL sends a request to the URL
displays the value of variable X-Request-Id in response header
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
