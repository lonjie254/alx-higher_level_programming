#!/usr/bin/python3

""" 
a function that creates an Object from a “JSON file” 
"""
import json


def load_from_json_file(filename):
    """loads the object from its json representation of the string"""
    with open(filename, 'r', encoding="utf-8") as myFile:
        return json.load(myFile)
