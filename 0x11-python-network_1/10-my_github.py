#!/usr/bin/python3
"""
This script fetches github ID using
Basic Authentication with a personal access token
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {'Authorization': 'token {}'.format(token)}

    response = requests.get(url, headers=headers)

    data = response.json()
    github_id = data.get('id')
    print(github_id)
