#!/bin/bash
# This script takes URL sends request to that URL and displays the size of the body of the response
# Usage: ./script_name.sh <URL>

url=$1
size=$(curl -w "%{size_download}\n" -o /dev/null -sS "$url")
echo "$size"
