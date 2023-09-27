#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept
curl -X OPTIONS -sI "$1" | grep "Allow:" | awk -F ": " '{print $2}'
