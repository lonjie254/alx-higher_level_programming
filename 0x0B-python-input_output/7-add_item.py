#!/usr/bin/python3

"""a script that adds all arguments to a
Python list, and then save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    class Run:
        arg_list = []

        def __init__(self):
            self.arg_list.extend(sys.argv[1:])
            filename = "add_item.json"
            save_to_json_file(self.arg_list, filename)

            self.arg_list = load_from_json_file(filename)
    a = Run()

"""ALTERNATE METHOD
import os
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = 'add_item.json'
args = len(sys.argv)
if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('[]')
if args > 1:
    data = load_from_json_file(filename)
    for i in range(1, args):
        data.append(sys.argv[i])
    save_to_json_file(data, filename)"""
