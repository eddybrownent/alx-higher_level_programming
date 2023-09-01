#!/usr/bin/python3
"""
This script takes a URL and an email address sends a POST request 
with the email as a parameter and finally displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)

    print(response.text)
