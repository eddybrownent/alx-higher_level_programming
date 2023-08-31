#!/usr/bin/bash
# This script that takes URL sends a GET request to the URL and displays the body of the response
curl -sL -w "%{http_code}" -o /dev/null "$1" | grep -q 200 && curl -sL "$1"
