#!/usr/bin/python3
""" Script that fetches the 'X-Request-Id' header value from a given URL """
import urllib.request
import sys


if __name__ == "__main__":
    """ Use a with statement to open the URL """
    with urllib.request.urlopen(sys.argv[1]) as html:
        request_id = html.headers.get('X-Request-Id')
        print(request_id)
