#!/usr/bin/python3
"""
This script adds all arguments to a Python list
and then save them to a file
"""
import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

for arguments in sys.argv[1:]:
    json_list.append(arguments)

save_to_json_file(json_list, filename)
