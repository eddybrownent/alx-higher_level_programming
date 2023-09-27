#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    responce = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(responce.text)))
    print("\t- content: {}".format(responce.text))
