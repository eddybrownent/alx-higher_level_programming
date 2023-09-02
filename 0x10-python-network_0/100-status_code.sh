#!/bin/bash
# This script Sends GET request to a URL and display response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
