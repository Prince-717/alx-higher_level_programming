#!/usr/bin/python3
"""Python module that adds all arguments to a Python list and save them to a file."""

import sys

if __name__ == "__main__":
    save_file_json = __import__('5-save_file_json').save_file_json
    load_file_json = \
        __import__('6-load_file_json').load_file_json

    try:
        item_list = load_file_json("add_item.json")
    except FileNotFoundError:
        item_list = []
    item_list.extend(sys.argv[1:])
    save_file_json(item_list, "add_item.json")
