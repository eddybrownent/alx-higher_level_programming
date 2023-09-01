#!/usr/bin/python3
"""
This script takes a letter sends POST request http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        payload = {'q': ""}
    else:
        payload = {'q': sys.argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    parsed = response.json()

    try:
        if parsed == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed.get('id'), parsed.get('name')))
    except ValueError:
        print("Not a valid JSON")
