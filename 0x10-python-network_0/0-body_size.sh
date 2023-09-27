#!/bin/bash
# This script takes URL sends request to that URL and displays the size of the body of the response
curl -w "%{size_download}\n" -o /dev/null -sS "$1"
